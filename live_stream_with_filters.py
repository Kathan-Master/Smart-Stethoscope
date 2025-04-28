import sys
import serial
import numpy as np
import pyaudio
import wave
import threading
import time
from scipy.signal import butter, lfilter
from scipy.fftpack import fft
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Serial Port Configuration
SERIAL_PORT = "COM10"  # Change for Linux/macOS (e.g., "/dev/ttyUSB0")
BAUD_RATE = 921600
SAMPLE_RATE = 8000
BUFFER_SIZE = 256
OUTPUT_FILENAME = "recorded_audio.wav"

# Initialize Serial Communication
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# PyAudio Configuration
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE, output=True)

# Recording Setup
wavefile = None
recording = False
streaming = False
start_time = 0
filter_mode = "None"  # Default no filter


def butter_filter(data, filter_type, lowcut=50, highcut=500, fs=8000, order=5):
    """Applies Butterworth filter (low-pass, high-pass, or band-pass)."""
    nyquist = 0.5 * fs
    if filter_type == "low":
        cutoff = lowcut / nyquist
        b, a = butter(order, cutoff, btype='low')
    elif filter_type == "high":
        cutoff = highcut / nyquist
        b, a = butter(order, cutoff, btype='high')
    elif filter_type == "band":
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(order, [low, high], btype='band')
    else:
        return data  # No filtering

    return lfilter(b, a, data)


class AudioStreamApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ESP32 Live Audio Stream with FFT")
        self.setGeometry(100, 100, 800, 600)

        # Layout
        self.layout = QVBoxLayout()
        self.label = QLabel("Live Audio Streaming from ESP32")
        self.layout.addWidget(self.label)

        # Start/Stop Buttons
        self.btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Streaming")
        self.start_btn.clicked.connect(self.start_stream)
        self.btn_layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("Stop Streaming")
        self.stop_btn.clicked.connect(self.stop_stream)
        self.stop_btn.setEnabled(False)
        self.btn_layout.addWidget(self.stop_btn)

        self.record_btn = QPushButton("Start Recording")
        self.record_btn.clicked.connect(self.toggle_recording)
        self.record_btn.setEnabled(False)
        self.btn_layout.addWidget(self.record_btn)

        self.layout.addLayout(self.btn_layout)

        # Recording Time Label
        self.recording_time_label = QLabel("Recording Time: 0 sec")
        self.layout.addWidget(self.recording_time_label)

        # Filter Buttons
        self.filter_layout = QHBoxLayout()
        self.lowpass_btn = QPushButton("Low-Pass Filter")
        self.lowpass_btn.clicked.connect(lambda: self.set_filter("low"))
        self.filter_layout.addWidget(self.lowpass_btn)

        self.highpass_btn = QPushButton("High-Pass Filter")
        self.highpass_btn.clicked.connect(lambda: self.set_filter("high"))
        self.filter_layout.addWidget(self.highpass_btn)

        self.bandpass_btn = QPushButton("Band-Pass Filter")
        self.bandpass_btn.clicked.connect(lambda: self.set_filter("band"))
        self.filter_layout.addWidget(self.bandpass_btn)

        self.clear_filter_btn = QPushButton("Clear Filter")
        self.clear_filter_btn.clicked.connect(lambda: self.set_filter("None"))
        self.filter_layout.addWidget(self.clear_filter_btn)

        self.layout.addLayout(self.filter_layout)

        # Matplotlib Figure for Audio Waveform and FFT
        self.figure, (self.ax_waveform, self.ax_fft) = plt.subplots(2, 1, figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

        # Timers
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

        self.record_timer = QTimer()
        self.record_timer.timeout.connect(self.update_recording_time)

        # Buffer for storing audio data
        self.audio_data = np.zeros(BUFFER_SIZE)

    def set_filter(self, mode):
        """Change the current filter mode."""
        global filter_mode
        filter_mode = mode
        print(f"Filter mode set to: {filter_mode}")

    def start_stream(self):
        global streaming
        streaming = True
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.record_btn.setEnabled(True)

        # Start reading audio in a separate thread
        threading.Thread(target=self.read_serial, daemon=True).start()
        self.timer.start(50)  # Update plot every 50ms

    def stop_stream(self):
        global streaming, recording
        streaming = False
        recording = False

        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.record_btn.setEnabled(False)

        if wavefile:
            wavefile.close()

        self.record_timer.stop()
        self.recording_time_label.setText("Recording Time: 0 sec")

    def toggle_recording(self):
        global recording, wavefile, start_time
        recording = not recording
        if recording:
            self.record_btn.setText("Stop Recording")
            wavefile = wave.open(OUTPUT_FILENAME, 'wb')
            wavefile.setnchannels(1)
            wavefile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wavefile.setframerate(SAMPLE_RATE)

            # Start recording time
            start_time = time.time()
            self.record_timer.start(1000)  # Update every second
        else:
            self.record_btn.setText("Start Recording")
            if wavefile:
                wavefile.close()
                print(f"Recording saved as {OUTPUT_FILENAME}")

            self.record_timer.stop()
            self.recording_time_label.setText("Recording Time: 0 sec")

    def update_recording_time(self):
        elapsed_time = int(time.time() - start_time)
        self.recording_time_label.setText(f"Recording Time: {elapsed_time} sec")

    def read_serial(self):
        global wavefile
        while streaming:
            data = ser.read(BUFFER_SIZE * 2)  # Read raw PCM data
            if data:
                samples = np.frombuffer(data, dtype=np.int16)

                # Apply selected filter
                if filter_mode == "low":
                    samples = butter_filter(samples, "low", lowcut=300)
                elif filter_mode == "high":
                    samples = butter_filter(samples, "high", highcut=500)
                elif filter_mode == "band":
                    samples = butter_filter(samples, "band", lowcut=500, highcut=1500)

                # Play the filtered audio
                stream.write(samples.astype(np.int16).tobytes())

                if recording and wavefile:
                    wavefile.writeframes(samples.astype(np.int16).tobytes())

                # Store data for visualization
                self.audio_data = samples
            time.sleep(0.01)

    def update_plot(self):
        self.ax_waveform.clear()
        self.ax_waveform.plot(self.audio_data, color="blue")
        self.ax_waveform.set_ylim(-500, 500)
        self.ax_waveform.set_title("Waveform")

        fft_data = np.abs(fft(self.audio_data))[:BUFFER_SIZE // 2]
        freqs = np.fft.fftfreq(BUFFER_SIZE, d=1 / SAMPLE_RATE)[:BUFFER_SIZE // 2]

        self.ax_fft.clear()
        self.ax_fft.plot(freqs, fft_data, color="red")
        self.ax_fft.set_title("FFT Spectrum")

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioStreamApp()
    window.show()
    sys.exit(app.exec())

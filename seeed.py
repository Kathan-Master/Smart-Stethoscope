import asyncio
import threading
from bleak import BleakScanner, BleakClient
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.signal import butter, lfilter

AUDIO_UUID = "87654321-4321-4321-4321-ba0987654321"
DEVICE_NAME = "SS_POC"
SAMPLE_RATE = 16000  # Full sampling rate, no downsampling
BUFFER_SIZE = 240

# ✅ Band-pass filter design
def design_bandpass_filter(fs, lowcut, highcut, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_bandpass_filter(data, fs, lowcut=50.0, highcut=300.0, order=5):
    b, a = design_bandpass_filter(fs, lowcut, highcut, order)
    return lfilter(b, a, data)

class BLEMicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎙 BLE Mic Band-Pass Stream")
        self.root.geometry("900x600")
        self.device = None
        self.client = None
        self.audio_buffer = []
        self.plot_buffer = np.zeros(2048, dtype=np.int16)

        # UI Elements
        self.label = ttk.Label(root, text="🔗 Click 'Connect' to start BLE Mic Stream", font=("Segoe UI", 14))
        self.label.pack(pady=10)

        self.connect_button = ttk.Button(root, text="Connect BLE Mic", command=self.run_async_thread)
        self.connect_button.pack(pady=5)

        self.canvas_frame = ttk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(8, 3))
        self.line, = self.ax.plot(self.plot_buffer)
        self.ax.set_ylim(-500, 500)
        self.ax.set_xlim(0, len(self.plot_buffer))
        self.ax.set_title("Live Audio Waveform (Band-Pass Filtered)")
        self.ax.set_xlabel("Sample Index")
        self.ax.set_ylabel("Amplitude")
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.root.after(50, self.update_plot)

        self.stream = sd.OutputStream(samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        self.stream.start()

    def update_plot(self):
        self.line.set_ydata(self.plot_buffer)
        self.canvas.draw()
        self.root.after(50, self.update_plot)

    def handle_audio_data(self, sender, data):
        samples = np.frombuffer(data, dtype=np.int16).astype(np.float32)

        # ✅ Apply band-pass filter
        samples = apply_bandpass_filter(samples, fs=SAMPLE_RATE, lowcut=300.0, highcut=600.0)

        # ✅ Clip and convert to int16
        samples = np.clip(samples, -32768, 32767).astype(np.int16)

        # Update buffer
        self.audio_buffer.extend(samples.tolist())
        self.plot_buffer = np.roll(self.plot_buffer, -len(samples))
        self.plot_buffer[-len(samples):] = samples

        if len(self.audio_buffer) >= BUFFER_SIZE:
            chunk = np.array(self.audio_buffer[:BUFFER_SIZE], dtype=np.int16)
            self.stream.write(chunk)
            del self.audio_buffer[:BUFFER_SIZE]

    async def start_stream(self):
        self.label.config(text="🔍 Scanning for BLE device...")
        device = None
        devices = await BleakScanner.discover(timeout=5.0)
        for d in devices:
            if d.name == DEVICE_NAME:
                device = d
                break

        if not device:
            self.label.config(text="❌ Device not found")
            return

        self.label.config(text=f"✅ Connected: {device.name}")

        async with BleakClient(device.address) as client:
            await client.start_notify(AUDIO_UUID, self.handle_audio_data)
            while True:
                await asyncio.sleep(0.01)

    def run_async_thread(self):
        threading.Thread(target=lambda: asyncio.run(self.start_stream()), daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = BLEMicApp(root)
    root.mainloop()

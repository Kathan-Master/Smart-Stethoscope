<h1>ABSTRACT<h1>
  Developed a smart stethoscope using an INMP441 mic and ESP32, later switching to XIAO nRF52840 for better BLE and low power. 
  We focused on noise filtering, real-time audio streaming via Python, and added features like heart rate, oximetry, and temperature monitoring. 

<h1>Smart Stethoscope<h1>
4.1 Study of Smart Stethoscope 
	I did extensive Online Research and Meetings to talk and learn about Current system in Smart Stethoscope solutions being used in India and Overseas.
	I check sample module of Smart Stethoscope given by We Hear company which originally sample product was made in Korea and check it working of device using application made by them.  In Smart Stethoscope there are three different things used to measure like heart, lungs and abdomen. There is MEMS microphone used in Stethoscope to measure sound inside of body via diaphragm. In this Stethoscope there was also a function to listen manually like using 3.5mm headphone jack. 
	I also check different types of Digital Stethoscope available in market and research on that. In research I found that application they developed also had AI-ML trained model where I check whether my heart beat is in good condition or it is pumping properly also it check whether the lungs inhale exhale is properly by human body or not.
	I also studied financial cost of such projects available in market. The cost of this type of project is very high but all product is made by different countries. 
4.2 Research & Working of Smart Stethoscope Module 
 
Figure 10: Top & Bottom View of Smart Stethoscope
4.3 Key Feature of this Stethoscope
	Measure with a smart stethoscope 
•	Lung (breathing) (60Hz – 400Hz) and heart measurement (50Hz – 300Hz) 
•	Measured data transmission through Bluetooth 
	Store, analyse, monitor using smartphone apps. 
•	2-types of app: Skeeper Pro (home), Skeeper Doctor (hospital) 
•	Analysis, History monitoring, Transmission to remote places
•	Also had support 3.5mm headphone jack for listening.
	Share the measured data, Doctor’s diagnosis 
•	Non-face-to-face treatment at the hospital (COVID-19) 
•	Transmit the measured data using e-mail or SNS 
•	Best for telemedicine service
•	Also download & share .wav file. 
 
Figure 11: Working of Stethoscope
Here the working of Stethoscope Module in which there are 2 Digital MEMS microphone are used in which one MEMS microphone is enclosed to diaphragm and another used for ANC Active Noise Canceling for background noise and body sound of own device while holding.
Bluetooth module is used as microcontroller here in which 2 Digital MEMS microphone data is taken and send one data over Bluetooth another data in CODEC when we connect Headphone Jack.
In application side AI-ML data trained to check your heart is healthy or not and also check as per user has health related problem also give lungs problem.



4.4 Technology and Literature Review
	Current Technology Exists 
	AiSteth
The AiSteth™ platform represents cutting-edge technology in the age of digital innovation. AiSteth™ encompasses the complete platform, incorporating the smart stethoscope, the accompanying mobile application, and the AI module. AiSteth™ is an Ai-enabled smart stethoscope that helps you see the sound on your smartphone and detect anomalies with the help of Artificial Intelligence (AI) and Machine Learning (ML) integration. Its purpose is to offer smart features through a mobile application, enabling you to record, store and share bodily sounds. 
	Keikku Heath
From to the precision of and the intuitive implementation of , every element is designed to enhance the act of Experience the, uncover health insights and elevate care to new  heights with Keikku. 
 
Figure 13: Keikku Heath

	Literature Review
1.	The Relationship between Normal Lung Sounds, Age, and Gender by Volker Gross, Anke Dittmar, Thomas Penzel, Frank Schüttler, And Peter Von Wichert
	Auscultation is one of the most important non-invasive and feasible methods for the detection of lung diseases. Systematic changes in breathing sounds with increasing age are of diagnostic importance. To investigate these changes, we recorded lung sounds taken from four locations in the posterior thorax of 162 subjects, together with airflow. The data were analysed according to age, sex, and smoking habit. In order to describe the power spectrum of the lung sounds, we calculated mean and median frequency, frequency with the highest power, and a ratio (Q) of relative power of the two frequency bands of 330 to 600 Hz and 60 to 330 Hz. Linear regression analysis was used as a measurement of age dependence of these variables. Significant differences in Q were found in men versus women (p, 0.05), but not in smokers versus nonsmokers. Within the groups, a small but significant correlation existed between Q and age (r2 < 0.1, p, 0.05). For both men and women, a slight increase of the relative power in the frequency band of 330 to 600 Hz was recorded with increasing age. How ever, on the basis of large individual variations, these small changes (DQ z 5%, SD(Q) > 6 5%) have no clinical significance and need not to be considered in the automatic detection of lung diseases by analysing lung sounds.

2.	Real-Time Smart-Digital Stethoscope System for Heart Diseases Monitoring by Muhammad E.H. Chowdhury, Amith Khandakar, Khawla Alzoubi, Samar Mansoor, Anas M. Tahir, Mamun Bin Ibne Reaz, Nasser Al-Emadi
	One of the major causes of death all over the world is heart disease or cardiac dysfunction. These diseases could be identified easily with the variations in the sound produced due to the heart activity. These sophisticated auscultations need important clinical experience and concentrated listening skills. Therefore, there is an un met need for a portable system for the early detection of cardiac illnesses. This paper proposes a prototype model of a smart digital-stethoscope system to monitor patient’s heart sounds and diagnose any abnormality in a real-time manner. This system consists of two subsystems that communicate wirelessly using Bluetooth low energy technology: A portable digital stethoscope subsystem, and a computer-based decision-making subsystem. The portable subsystem captures the heart sounds of the patient, filters and digitizes, and sends the captured heart sounds to a personal computer wirelessly to visualize the heart sounds and for further processing to make a decision if the heart sounds are normal or abnormal. Twenty-seven t-domain, f-domain, and Mel frequency cepstral coecients (MFCC) features were used to train a public database to identify the best-performing algorithm for classifying abnormal and normal heart sound (HS). The hyper parameter optimization, along with and without a feature reduction method, was tested to improve accuracy. The cost-adjusted optimized ensemble algorithm can produce 97% and 88% accuracy of classifying abnormal and normal HS, respectively.


3.	Digital Stethoscope Use in Neonates: A Systematic Review by Meagan Roff1, Olivia Slifirski1, Ethan Grooby, Faezeh Marzbanrad, Atul Malhotra
	A systematic review and narrative synthesis of studies published between January 1, 1990 and May 29, 2023 was conducted following searches of MEDLINE, Embase, PubMed, Scopus, and Google Scholar databases, as well as trial registries. Results: Of 3,852 records identified, a total of 41 papers were eligible and included in the narrative synthesis. Thirteen records were non-full-text articles, either in the form of journal letters or conference abstracts, and these were included separately for completion purposes but may be unreliable. Digital stethoscopes have been studied in neonatology across various clinical areas, including artificial intelligence for sound quality assessment and chest sound separation (n = 5), cardiovascular sounds (n = 11), respiratory sounds (n = 4), bowel sounds (n = 4), swallowing sounds (n = 2), and telemedicine (n = 2). This paper discusses the potential utility of digital stethoscope technology for the interpretation of neonatal sounds for both humans and artificial intelligence. The limitations of current devices are also assessed.
 
CHAPTER 5: SYSTEM DESIGN ON SMART STETHOSCOPE 
5.1 Prototype on ESP32
After Researching the module, I start making the prototype on ESP32 using I2S (Inter-Integrated Circuit Sound) protocol using single microphone INMP441 module and get the data of microphone on Laptop using python script which read the microphone data and listen live streaming on laptop.
After getting the data on laptop of microphone we send over Bluetooth using app call DumbDisplay. We attached a diaphragm on microphone and listen the sound of my heart on application and also record the microphone in application.
5.2 Why INMP441 MEMS Microphone is used?
The INMP441 is a high-performance, low power, digital-output, omnidirectional MEMS microphone with a bottom port. The complete INMP441 solution consists of a MEMS sensor, signal conditioning, an analog-to-digital converter, anti-aliasing filters, power management, and an industry-standard 24-bit I²S interface. The I²S interface allows the INMP441 to connect directly to digital processors, such as DSPs and microcontrollers, without the need for an audio codec in the system. The INMP441 has a high SNR, making it an excellent choice for near field applications. The INMP441 has a flat wideband frequency response, resulting in natural sound with high intelligibility.
 	 
Figure 15: INMP441 MEMS MIC
5.3 Specification:
Table 1: INMP441 Microphone Specification
Frequency Range (Hz):	20 to 20000
S/N Ratio (dB)	61 dBA
High Sensitivity	-26 dBFS
Current Consumption (mA):	1.4 mA
High Power Supply Rejection	-75 dBFS
Directionally	Omnidirectional
Voltage (DC)	1.8 – 3.3 V

5.4 MEMS Microphone
Electret condenser microphone (ECM) counterpart, MEMS microphones extract audio pressure changes as electrical signals. However, MEMS microphones boast a reliable monolithic structure and far more compact form factor, which significantly lowers mechanical vibration, power consumption, and noise interference. They also offer a better signal-to-noise ratio (SNR) and support a wide operating temperature range.
MEMS microphones, also known as silicon microphones, are now commonly used in smartphones, tablets, laptops, hearing aids, voice biometric, digital voice assistants, and more.
MEMS microphone comprises a flexibly suspended diaphragm free to move above a fixed backplate and is fabricated on a silicon wafer. When a sound pressure passes through holes in the backplate, it causes the diaphragm to move in proportion to the sound wave’s amplitude. The movement varies the distance between the diaphragm and the backplate, and that varies the capacitance. Here, a semiconductor device converts the change in capacitance into an electrical signal.
 
Figure 16: MEMS Top Microphone
MEMS microphones are available as both analog or digital devices. The chip inside the MEMS microphone can provide electric signals either in differential analog or digital format at the output. 
Design examples include simple loudspeakers and radio communication systems. While analog MEMS microphones offer a simple and straightforward interface to the host device, analog signals mandate careful design to eliminate noise between the microphone output and the input of the IC receiving the signal.
On the other hand, digital MEMS microphones convert analog voltage signals into a digital bitstream using an analog-to-digital converter (ADC) followed by encoding with pulse density modulation (PDM) technique. Typically, digital MEMS microphones are more suitable for designs where the host is a microcontroller (MCU) or a digital signal processor (DSP). Digital MEMS microphones also offer better noise immunity, bit error tolerance, and a simple hardware interface.
 
Figure 17: MEMS Bottom Microphone.
The decision between choosing an analog or digital MEMS microphone often depends on the end application. Especially, how the end application is going to use the output signal.
	Advanced features
MEMS microphones, now a key enabler in human-machine communication, are becoming a major building block in voice-enabled applications. For instance, STMicroelectronics has incorporated its MEMS microphone into a system-in-package (SiP) that integrates DSP Group’s ultra-low-power voice processors and Sensory’s voice recognition firmware. The design is aimed at voice-activated appliances such as smart speakers, TV remotes, wearables, and smart home systems.
MEMS microphone’s dramatic enhancement of sound quality made available in a small form factor also makes it a popular component in microphone arrays targeted at applications like concert halls, television broadcasting, and surveillance systems. The arrays of MEMS microphones are employed to significantly improve the quality of sound while creating a more directional response.
5.5 I2S – Inter-Integrated Circuit Sound
The protocol which is used to transmit digital audio data from one device to another device is known as I2S or Inter-IC Sound protocol. This protocol transmits PCM (pulse-code modulated) audio data from one IC to another within an electronic device. I2S plays a key role in transmitting audio files which are pre-recorded from an MCU to a DAC or amplifier. This protocol can also be utilized to digitize audio using a microphone. There is no compression within I2S protocols, so you cannot play OGG or MP3 or other audio formats that condense the audio, however, you can play WAV files.
5.6 Features of I2S
•	It has 8 to 32 data bits for each sample.
•	Tx & Rx FIFO interrupts.
•	It supports DMA.
•	16-bit, 32-bit, 48-bit, or 64-bit word select period.
•	Simultaneous bi-directional audio streaming.
•	8-bit, 16-bit, and 24-bit sample width.
•	It has different sample rates.
•	The data rate is up to 96 kHz through the 64-bit word select period.
•	Interleaved stereo FIFOs or Independent right & left channel FIFOs
•	Independent enable of Tx & Rx.
5.7 3-Wire Connection of I2S:
	SCK - The SCK or Serial Clock is the first line of the I2S protocol which is also known as BCLK or bit clock line which is used to obtain the data on a similar cycle. The serial clock frequency is simply defined by using the formula like 
	WS - In the I2S communication protocol, the WS or word select is the line which is also known as FS (Frame Select) wire that separates the right or left channel.
•	If WS = 0 then left channel or channel-1 is used.
•	If WS = 1 then the right channel or channel-2 is used.
	SD - The Serial Data or SD is the last wire where the payload is transmitted within 2 complements. So, it is very significant that the MSB is first transferred, because both the transmitter & receiver may include different word lengths. Thus, the transmitter or the receiver has to recognize how many bits are transmitted.
•	If the word length of the receiver is greater than the transmitter, then the word is shortened (LSB bits are set to zero).
•	If the word length of the receiver is less than the word length of the transmitter, then the LSB bits are ignored.
The transmitter can sent the data either on the leading edge or trailing edge of the clock pulse. This can be configured in the corresponding control registers. But the receiver latches the serial data and WS only on the leading edge of the clock pulse. The transmitter transmits data only after one clock pulse after change in WS.  The receiver uses the WS signal for synchronisation of the serial data.
5.8 I2S Master & Slave Mode
 
Figure 18: I2S Master and Slave Mode
•	In the first diagram, the transmitter (Tx) is the master so it controls the SCK (serial clock) & WS (word select) lines.
•	In the second diagram, the receiver is the master. So both the SCK & WS lines start from the receiver & the transmitter ends.
•	In the third diagram, an exterior controller is connected to the nodes within the network which works like the master device. So this device generates the SCK & WS.
•	In the above-all I2S networks, there is only a single master device available and many other components that transmit or receive sound data.
•	In I2S any device can be the master by providing the clock signal.
5.9 I2S Timing Diagram
For a better understanding of the I2S & its functionality, we have the I2S communication protocol timing diagram shown below. The timing diagram of the I2S protocol is shown below which includes three wires SCK, WS & SD.
 
 
Figure 19: Inter-Integrated Circuit Sound
5.10 Interface definition:
1.	SCK: Serial data clock for I2S interface
2.	WS: Serial data word selection for I2S interface
3.	L/R: Left/Right channel selection.
4.	When set to low, the microphone outputs a signal on the left channel of the I2S frame.
5.	When set to high level, the microphone outputs signals on the right channel
6.	SD: Serial data output of the I2S interface.
7.	VCC: Input power, 1.8V to 3.3V.
8.	GND: power ground
5.11 Connection Diagram 
 
Figure 20: INMP441 with ESP32 Connection
	Pin Connection

Table 2: Pin Connection
ESP32	INMP441 Microphone
GPIO 25	WS – Word Select
GPIO 32	SCK – Serial Clock
GPIO 33	SD – Serial Data
3.3V	VCC – Input Power Supply
GND	GND – Ground
GND	L/R – Left or Right Channel Selection

5.12 Achievement on ESP32 prototype: 
 
Figure 21: HeartBeat Wave-form using Python Script
Here the above image shows us heartbeat waveform and also have analysis spectrum using FFT in python script. In python script we add Recording feature to listen the heartbeat using our stethoscope. Recording of heartbeat was done in .wav File format.
In this python script we also added filter LOWPASS, HIGHPASS & BANDPASS Filters in it.
5.13 Hardware Implementation 
 
Figure 22: Prototype on ESP32
Above image is the prototype interface to listen the beat of heart on python script. I had integrated the Bluetooth for listening heartbeat sound on mobile application named as DumbDisplay.

 	 
Figure 23: Dumb Display Application 
Here the streaming of data sends using Bluetooth on application called as DumbDisplay. The Red Dot seeing here are Heart Beat maximum and minimum value shown in display. There is terminal where device name of Bluetooth as ESP32BT.
CHAPTER 6: IMPLEMENTATION
6.1 XIAO Seeed Studio NRF52840 Implementation  
I implemented a real-time audio data streaming solution using the Seeed Studio nRF52840 development board, which features an integrated PDM (Pulse-Density Modulation) microphone. The primary goal was to capture ambient sound and stream microphone data over Bluetooth Low Energy (BLE) to a mobile device, specifically the nRF Connect mobile application.
This project emphasized real-time embedded systems design, BLE protocol tuning, and microphone signal acquisition — blending multiple layers of hardware and software development into one coherent system.
6.2 Features on NRF52840
•	Powerful wireless capabilities: Bluetooth 5.0 with onboard antenna
•	Powerful CPU: Nordic nRF52840, ARM® Cortex®-M4 32-bit processor with FPU, 64 MHz
•	Ultra-Low Power: Standby power consumption is less than 5μA
•	Battery charging chip: Supports lithium battery charge and discharge management
•	Onboard 2 MB flash
•	Onboard PDM microphone (only in Seeed Studio XIAO nRF52840 Sense)
•	Onboard 6-axis LSM6DS3TR-C IMU (only in Seeed Studio XIAO nRF52840 Sense)
•	Ultra Small Size: 21 x 17.8mm, Seeed Studio XIAO series classic form-factor for wearable devices
•	Rich interfaces: 1xUART, 1xI2C, 1xSPI, 1xNFC, 1xSWD, 11xGPIO(PWM), 6xADC in XIAO nRF52840 (Sense); and 2xUART, 1xI2C, 2xSPI, 1xI2S, 1xNFC, 1xSWD, 18xGPIO(PWM), 6xADC in XIAO nRF52840 (Sense) Plus
•	Single-sided components, surface mounting design





6.3 Specification on XIAO NRF52840
Table 3: XIAO SEEED STUDIO NRF52840
Processor	Nordic nRF52840, ARM® Cortex®-M4 32-bit processor with FPU, 64 MHz
Wireless Connectivity	Bluetooth 5.0/BLE/NFC
Memory	256 KB RAM,1MB Flash 2MB onboard Flash
Built-in Sensors	6 DOF IMU (LSM6DS3TR-C), PDM Microphone
Interfaces	1xI2C, 1xUART, 1xSPI
PWM/Analog Pins	11/6
Onboard Buttons	Reset Button
Onboard LEDs	3-in-one LED/ Charge LED
Battery Charge Chip	BQ25101
Programming Languages	Arduino/ MicroPython/ CircuitPython

6.4 Why Shift to XIAO NRF52840 not ESP32
Table 4: XIAO NRF52840 vs ESP32
	XIAO NRF52840	ESP32
Processor	ARM Cortex-M4F @ 64 MHz (with FPU)

	Dual-core Xtensa LX6 @ 240 MHz


Power Consumption	Ultra-low (active: ~4–10 mA, sleep: ~1.5 µA)	Higher (active: ~80–240 mA)
BLE Support	BLE 5.0 (Long Range, Low Energy)	Classic + BLE 4.2


Audio Streaming	BLE custom GATT streaming supported	Bluetooth Classic (A2DP), not BLE-friendly
ADC Support	12-bit ADC with clean analog support

	12-bit ADC (with some noise)
Battery Management	Built-in LiPo charging + battery monitor

	External circuitry needed

6.5 Microphone Interface
The onboard PDM microphone of the Seeed Studio nRF52840 board was configured using Nordic SDK’s nrfx_pdm driver. Depending on the BLE stack used, Tiny USB support was optionally included.
A DMA-based double buffering technique ensured efficient mic data sampling without blocking the CPU, providing smooth real-time data acquisition.
 
Figure 24: XIAO SEEED STUDIO NRF52840
6.6 BLE Transmission
A custom GATT service was created with a notify-enabled characteristic. Microphone data was packetized into 20-byte chunks to respect the BLE MTU limit. Streaming was triggered only after a BLE central device (like a smartphone) successfully connected. The connection interval, MTU size, and notification rates were tuned for maximum throughput and reliability. 
 
Figure 25: BLE Device
6.7 Mobile App Interface
The nRF Connect mobile app was used to scan, connect, and receive BLE notifications. Audio data was visualized in hex format or exported for offline analysis. A future extension may include a custom mobile app with waveform rendering or basic audio playback.
 
Figure 26: NRF Connect Application
6.8 Challenges and Solutions
BLE Throughput Limitations
1.	The audio signal was down sampled to reduce the data rate. BLE connection parameters were optimized for higher throughput.
2.	Application connection due to UUID create the connected as client.
3.	Convert HEX data value of mic to digital data using python Script
7.9 Simultaneous Debug Output
For development: The system was configured to stream microphone data both over BLE and Serial.
 
Figure 27: BLE interface with xiao using python script
This allowed live monitoring via Serial Plotter or logging in VS Code, ensuring real-time debugging without affecting BLE performance.

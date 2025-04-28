#include <mic.h>
#include <ArduinoBLE.h>

// BLE Audio Service and Characteristic UUIDs
BLEService audioService("12345678-1234-1234-1234-1234567890ab");
BLECharacteristic audioChar("87654321-4321-4321-4321-ba0987654321", BLERead | BLENotify, 240);  // 240 bytes = 120 int16 samples

mic_config_t mic_config{
  .channel_cnt = 1,
  .sampling_rate = 16000,      // ✅ Changed from 16000 to 8000
  .buf_size = 240,            // ✅ 120 samples × 2 bytes = 240 bytes
  .debug_pin = LED_BUILTIN
};

NRF52840_ADC_Class Mic(&mic_config);

#define SAMPLES 120           // ✅ 120 samples at 8000 Hz = 15 ms of audio
int16_t recording_buf[SAMPLES];
volatile bool record_ready = false;

void setup() {
  Serial.begin(9600);

  if (!Mic.begin()) {
    Serial.println("Mic initialization failed");
    while (1);
  }
  Mic.set_callback(audio_rec_callback);
  Serial.println("Mic initialized");

  if (!BLE.begin()) {
    Serial.println("Starting BLE failed");
    while (1);
  }

  BLE.setLocalName("SS_POC");
  BLE.setAdvertisedService(audioService);
  audioService.addCharacteristic(audioChar);
  BLE.addService(audioService);
  BLE.advertise();

  Serial.println("BLE advertising started");
}

void loop() {
  BLEDevice central = BLE.central();
  if (central) {
    Serial.print("Connected to central: ");
    Serial.println(central.address());

    while (central.connected()) {
      if (record_ready) {
        record_ready = false;

        // Send raw audio buffer over BLE
        audioChar.writeValue((uint8_t*)recording_buf, sizeof(recording_buf));

        // Debug
        Serial.println("Sent audio data over BLE");
      }
    }

    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
}

static void audio_rec_callback(uint16_t *buf, uint32_t buf_len) {
  static uint32_t idx = 0;

  for (uint32_t i = 0; i < buf_len; i++) {
    recording_buf[idx++] = buf[i];
    if (idx >= SAMPLES) {
      idx = 0;
      record_ready = true;
      break;
    }
  }
}

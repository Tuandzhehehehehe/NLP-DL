#include <WiFi.h>
#include <WebSocketsClient.h>
#include "driver/i2s.h"

/* ================= CONFIG ================= */
#define WIFI_SSID     "YOUR_WIFI"
#define WIFI_PASS     "YOUR_PASS"

#define WS_HOST       "192.168.1.10"   // IP PC
#define WS_PORT       8765
#define WS_PATH       "/"

/* I2S config */
#define I2S_WS        5
#define I2S_SD        4
#define I2S_SCK       6

#define SAMPLE_RATE   16000
#define BUFFER_LEN    512   // samples

WebSocketsClient webSocket;

/* ================= I2S ================= */
void setupI2S() {
  i2s_config_t i2s_config = {
    .mode = (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_RX),
    .sample_rate = SAMPLE_RATE,
    .bits_per_sample = I2S_BITS_PER_SAMPLE_16BIT,
    .channel_format = I2S_CHANNEL_FMT_ONLY_LEFT,
    .communication_format = I2S_COMM_FORMAT_I2S,
    .intr_alloc_flags = ESP_INTR_FLAG_LEVEL1,
    .dma_buf_count = 8,
    .dma_buf_len = BUFFER_LEN,
    .use_apll = false
  };

  i2s_pin_config_t pin_config = {
    .bck_io_num = I2S_SCK,
    .ws_io_num = I2S_WS,
    .data_out_num = I2S_PIN_NO_CHANGE,
    .data_in_num = I2S_SD
  };

  i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
  i2s_set_pin(I2S_NUM_0, &pin_config);
}

void webSocketEvent(WStype_t type, uint8_t *payload, size_t length) {
  if (type == WStype_CONNECTED) {
    Serial.println("✅ WebSocket connected");
  }
}

/* ================= SETUP ================= */
void setup() {
  Serial.begin(115200);

  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n📶 WiFi connected");

  setupI2S();

  webSocket.begin(WS_HOST, WS_PORT, WS_PATH);
  webSocket.onEvent(webSocketEvent);
}

/* ================= LOOP ================= */
void loop() {
  static int16_t samples[BUFFER_LEN];
  size_t bytes_read;

  i2s_read(
    I2S_NUM_0,
    samples,
    sizeof(samples),
    &bytes_read,
    portMAX_DELAY
  );

  webSocket.sendBIN((uint8_t *)samples, bytes_read);
  webSocket.loop();
}

#define MQ2_PIN 34 // Or your chosen analog pin
#define LED_PIN 12 // For optional LED

void setup() {
  Serial.begin(115200); // Start serial communication
  pinMode(MQ2_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("MQ-2 Gas Sensor Test");
}

void loop() {
  int sensorValue = analogRead(MQ2_PIN); // Read analog value (0-4095 for ESP32)
  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);

  // Simple Alarm Logic
  if (sensorValue > 1000) { // Adjust this threshold later
    digitalWrite(LED_PIN, HIGH); // Turn on LED
  } else {
    digitalWrite(LED_PIN, LOW);  // Turn off LED
  }

  delay(1000); // Wait for a second
}


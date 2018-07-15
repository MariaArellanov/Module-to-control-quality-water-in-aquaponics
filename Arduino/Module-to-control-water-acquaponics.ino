#include <OneWire.h>
#include <DallasTemperature.h>

// Global variable declarations
///Ambient Temperature (LM35)///
float tempC; 
int pinLM35 = 0; 

//---Water Temperature (DS18B20)---//
OneWire ourWire(3); 
DallasTemperature sensors(&ourWire); 

///Water Flow (YF-S201)///
const int sensorPin = 2;
const int measureInterval = 2500;
volatile int pulseConter;

// Flow sensor conversion factors
const float factorK = 7.5; // YF-S201

// Interrupt Service Routine (ISR)
void ISRCountPulse() {
  pulseConter++;
}

// Function to calculate pulse frequency
float GetFrequency() {
  pulseConter = 0;
  interrupts();
  delay(measureInterval);
  noInterrupts();
  return (float)pulseConter * 1000 / measureInterval;
}

// --- Conversion Functions ---
float temperatura(float analogValue) {
  return (analogValue * 5.0 * 100.0) / 1024.0;
}

float flujoAgua(float hz) {
  return hz / factorK;
}

void setup() {
  // Serial port configured to 19200 to match Raspberry Pi script
  Serial.begin(19200); 
  
  attachInterrupt(digitalPinToInterrupt(sensorPin), ISRCountPulse, RISING);

  delay(1000);
  sensors.begin(); 
}

void loop() {
  // --- Ambient Temperature ---
  tempC = analogRead(pinLM35);
  float ambientTemp = temperatura(tempC);

  // Send with "ambi" tag for Python parsing
  Serial.print("ambi"); 
  Serial.println(ambientTemp);

  delay(1000);

  // --- Water Temperature ---
  sensors.requestTemperatures(); 
  float waterTemp = sensors.getTempCByIndex(0); 

  // Send with "watr" tag for Python parsing
  Serial.print("watr");
  Serial.println(waterTemp);
  
  delay(100);

  // --- Water Flow ---
  float frequency = GetFrequency(); 
  float flowRate = flujoAgua(frequency); 
  
  // Send with "pump" tag for Python parsing
  Serial.print("pump");
  Serial.println(flowRate);

  // Error handling example:
  if (flowRate <= 0) {
    Serial.println("error");
  }
}
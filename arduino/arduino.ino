#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);  // Set up the LCD's number of columns and rows:
  Serial.begin(9600);  // Start serial communication
}

void loop() {
  if (Serial.available()) {
    String receivedData = Serial.readString();
    int delimiterPosition = receivedData.indexOf(',');
    String tempCPU = receivedData.substring(0, delimiterPosition);
    String tempGPU = receivedData.substring(delimiterPosition + 1);

    displayTemperature(tempCPU, tempGPU);
  }
  delay(500);
}

void displayTemperature(String tempCPU, String tempGPU) {
  lcd.clear();  // Clear the LCD
  lcd.setCursor(0, 0);  // Set the cursor to top-left
  lcd.print("CPU: " + tempCPU + " C" );
  lcd.setCursor(0, 1);  // Set the cursor to the beginning of the second row
  lcd.print("GPU: " + tempGPU + " C" );
}

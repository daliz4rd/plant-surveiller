const int SENSOR_PIN = A0; //wiper pin
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //start talking to USB 9600 bits per second
}

void loop() {
  // put your main code here, to run repeatedly:
  int reading = analogRead(SENSOR_PIN); //get integer reading from the analog sensor indicated by the variable i made, SENSOR_PIN. I have it plugged into A0 on my board.
  Serial.println(reading); //Serial is an object the arduino library creates automatically representing board's serial (usb) connection. this sends the above to computer line by line
  delay(500); //wait 500ms
}

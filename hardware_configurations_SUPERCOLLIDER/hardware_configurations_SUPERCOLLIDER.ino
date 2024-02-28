void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  digitalWrite(LED_BUILTIN, HIGH);
  // print out the value you read:
  Serial.println(sensorValue);
  delay(1000);  // delay in between reads for stability
  digitalWrite(LED_BUILTIN, LOW);
}

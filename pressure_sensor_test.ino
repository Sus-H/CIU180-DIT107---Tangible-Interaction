#define PRESSURE_PIN A0;
float pressure = 0;

void setup() {
    Serial.begin(9600);
}

void loop{
    pressure = analogRead(PRESSURE_PIN);
    Serial.print("PRESSURE: ")
    Serial.println(pressure)
}

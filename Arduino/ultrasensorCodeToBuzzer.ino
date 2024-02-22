/*
  Use an ultrasensor to read distance.
  Then depending on the distance, lighting a lamp and making a buzzer sound.
*/

#define LED_PIN 13 // LED pin
#define BUZZER_PIN 8 // BUZZER pin
// ULTRASENSOR pins
const int trigPin = 9;
const int echoPin = 10;

int duration = 0;
float distance = 0;

void setup() {
  Serial.begin(9600);
  
  pinMode(echoPin, INPUT);
  pinMode(trigPin, INPUT);

  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
}


void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration * .0343) / 2;
  
  // prints the distance from the ultrasensor
  // Serial.print("distance ");
  // Serial.println(distance);
  delay(100);

  // detecting between distance A and B, and then do something
  if (distance < 20 && distance > 10) { 
    // Turn on the LED to help indicate that it works
    digitalWrite(LED_PIN, HIGH); 

    // turns of the buzzer for now
    tone(BUZZER_PIN, 50); 

  }
  // otherwise do not do anything
  else {
    // Turn off the LED
    digitalWrite(LED_PIN, LOW); 
    
    // turns off the buzzer
    noTone(BUZZER_PIN); 
  }
}

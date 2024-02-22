/*
  Use an ultrasensor to read distance.
  Then depending on the distance, lighting a lamp and making a buzzer sound.
*/
// Tone library?
#include <Arduino.h>
#define TONE_USE_INT
#define TONE_PITCH 440
#include <TonePitch.h>


#define LED_R_PIN 13 // red LED pin
#define LED_B_PIN 12 // blue LED pin
#define BUZZER_PIN 8 // BUZZER pin
#define SPEAKER_PIN 6 // SPEAKER pin
#define KNOB_PIN A0 // KNOB pin
#define KNOB_TINY_PIN A1 // KNOB tiny pin
// ULTRASENSOR pins
const int trigPin = 9;
const int echoPin = 10;

int duration = 0;
float distance = 0;

int knobValue = 0;
int tinyKnob = 0;

void setup() {
  // ULTRASENSOR
  pinMode(echoPin, INPUT);
  pinMode(trigPin, INPUT);

  // BUZZER
  pinMode(BUZZER_PIN, OUTPUT);
  // SPEAKER
  pinMode(SPEAKER_PIN, OUTPUT);
  // LED
  pinMode(LED_R_PIN, OUTPUT);
  pinMode(LED_B_PIN, OUTPUT);

  Serial.begin(9600);
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
  // delay(100);

  // Reading the knob value
  knobValue = analogRead(KNOB_PIN);
  tinyKnob = analogRead(KNOB_TINY_PIN);
  Serial.print("knob value ");
  Serial.println(knobValue);


  // Knob, do something
  if (knobValue > 700) {
    // Turn on the LED to help indicate that it works
    digitalWrite(LED_B_PIN, HIGH); 
    // Play a tone
    // tone(SPEAKER_PIN, NOTE_G3);
    Serial.println("tone1");

  }
  else if (knobValue > 300 && knobValue < 700) {
    // Blink with the light
    digitalWrite(LED_B_PIN, HIGH); 
    digitalWrite(LED_B_PIN, LOW);
    // Turn off the sound
    // noTone(SPEAKER_PIN);
    Serial.println("tone2");

  }
  else {
    // Turn of the light and sound
    digitalWrite(LED_B_PIN, LOW); 
    // noTone(SPEAKER_PIN);
    Serial.println("noTone");

  }


  // For the TINY knob, do something
  if (tinyKnob > 700) {

  }
  else if (tinyKnob > 300 && tinyKnob < 700) {

  }
  else {

  }

  // ultrasensor, do something
  // detecting between distance A and B, and then do something
  if (distance < 20 && distance > 10) { 
    // Turn on the LED to help indicate that it works
    digitalWrite(LED_R_PIN, HIGH); 

    // turns of the buzzer for now
    // tone(BUZZER_PIN, 50);

  }
  else if (distance < 10) {

  }
  // otherwise do nothing
  else {
    // Turn off the LED
    digitalWrite(LED_R_PIN, LOW); 
    // Serial.println("noTone");
    // turns off the buzzer
    // noTone(BUZZER_PIN); 
  }
  delay(100);
}

#include <Arduino.h>
#define TONE_USE_INT
#define TONE_PITCH 440
#include <TonePitch.h>


#define LED_R_PIN 13 // red LED pin
#define LED_B1_PIN 12 // blue LED pin
#define LED_W_PIN 11 // white LED pin
#define LED_B2_PIN 10 // second blue LED pin

#define TOUCH_PIN 7 // Touchpad

#define KNOB_0_PIN A0 // KNOB pin
#define KNOB_1_PIN A1 // KNOB tiny pin
#define KNOB_2_PIN A2 // KNOB tiny pin

#define PRESSURE_4_PIN A4 // PRESSURE SENSOR pin
#define SLIDER_5_PIN A5 // SLIDER pin

//PRESSURE SENSOR
int pressure_value = 0;

// ULTRASENSOR pins
const int echoPin = 10;
const int trigPin = 11;

int duration = 0;
float distance = 0;

// POTENTIOMETERS
int knob_0_value = 0;
int knob_1_value = 0;
int knob_2_value = 0;
int slider_5_value = 0;

int values[6];

void setup() {
  // ULTRASENSOR
  pinMode(echoPin, INPUT);
  pinMode(trigPin, INPUT);

  // TOUCHPAD
  // pinMode(TOUCH_PIN, INPUT);

  // LED
  /* pinMode(LED_R_PIN, OUTPUT);
  pinMode(LED_B1_PIN, OUTPUT);
  pinMode(LED_W_PIN, OUTPUT);
  pinMode(LED_B2_PIN, OUTPUT); */

  Serial.begin(9600);
}


void loop() {
  /* digitalWrite(LED_R_PIN, LOW); 
  digitalWrite(LED_B1_PIN, LOW); 
  digitalWrite(LED_W_PIN, LOW); 
  digitalWrite(LED_B2_PIN, LOW); */
  
  values[0] = play_tone();
  values[1] = volume();
  values[2] = instrument();
  values[3] = durations();
  values[4] = drum_sound();
  values[5] = pressure_sensor();

  for (int i = 0; i < 6; i++) {
    Serial.print(values[i]);
    Serial.print(" ");
  }
  Serial.println("");
  delay(1000/durations());
  
}


// Functions for the different components
// Ultra sonic sensor - different distance = different tone.
int play_tone() {
  
  // Send sonic waves, delay for time to send and read
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration * .0343) / 2;
  
  // up to 35 cm
  if (distance > 50) {
    return 0;
  }
  if (distance < 50) {
    return map(distance, 0, 50, 0, 14);
  }
}

// POTENTIOMETERS Values 0-1023
int volume() {
  slider_5_value = analogRead(SLIDER_5_PIN);
  return map(slider_5_value, 0, 1023, 0, 100);
}


int instrument() {
  knob_0_value = analogRead(KNOB_0_PIN);
  return map(knob_0_value, 0, 1023, 1, 11);
}


int durations() {
  knob_1_value = analogRead(KNOB_1_PIN);
  
  if (knob_1_value < 205) {
    return 1;
    }
  
  if (knob_1_value < 410) {
    return 2;
    }

  if (knob_1_value < 615) {
    return 2;
    }

  if (knob_1_value < 820) {
    return 4;
    }

  if (knob_1_value < 1023) {
    return 8;
    }
  else {
    return 8;
    }
}


int drum_sound() {
  knob_2_value = analogRead(KNOB_2_PIN);
  return map(knob_2_value, 0, 1023, 0, 1);
}

int pressure_sensor() {
  pressure_value = analogRead(PRESSURE_4_PIN);
  return pressure_value;
}


bool touchpad() {
  return digitalRead(TOUCH_PIN);
}


void webcam_module() {

}


void touchpad_LCD_module() {

}

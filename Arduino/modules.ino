

#define MIC_PIN A0 // Microphone pin
#define LED_PIN 13 // LED pin

int micValue = 0;

void setup() {
  Serial.begin(9600);
  
  pinMode(MIC_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}


void loop() {
  micValue = analogRead(MIC_PIN);
  Serial.println("micValue " + micValue);
  
  if (micValue > 100) { // If sound is detected
    /*
    tone(SPEAKER_PIN, toneFrequency); // Play the tone
    displayFrequencyWave(toneFrequency);
    displayNoteLetter(noteLetter);
    digitalWrite(LED_PIN, HIGH); // Turn on the LED
    delay(500); // Wait for a short duration
    digitalWrite(LED_PIN, LOW); // Turn off the LED
    noTone(SPEAKER_PIN); // Stop the tone
    */
    digitalWrite(LED_PIN, LOW); // Turn on the LED
    Serial.println("sound is DETECTED");
    
  }
  else {
    digitalWrite(LED_PIN, HIGH); // Turn off the LED
    Serial.println("sound NOT detected");
  }

  delay(500);
}

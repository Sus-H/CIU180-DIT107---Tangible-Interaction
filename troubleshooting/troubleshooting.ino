const int echoPin = 10;
const int trigPin = 11;

int duration = 0;
float distance = 0;

void setup() {
  // put your setup code here, to run once:
  // ULTRASENSOR
  pinMode(echoPin, INPUT);
  pinMode(trigPin, INPUT);
  Serial.begin(9600);



}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(play_tone());

}

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
  if (distance > 35) {
    return 0;
  }
  return map(distance, 0, 35, 58, 68);
}

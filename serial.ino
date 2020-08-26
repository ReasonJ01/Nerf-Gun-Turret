

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
   pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  if(Serial.available() > 0){
    if(Serial.read() == "s"){
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(1000);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);
    }
  }

}

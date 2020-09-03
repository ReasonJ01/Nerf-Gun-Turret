#include <Servo.h>
Servo servox;
Servo servoy;
int prevpos;
int pos;
String dataIn;



void setup() {
  // put your setup code here, to run once:
  Serial.setTimeout(10);
  Serial.begin(9600);
  servox.attach(9);
  servoy.attach(5);
  servox.write(90);
  servoy.write(90);
}


void loop() {
  //
}


void serialEvent() {
  while (Serial.available()) {
    dataIn = Serial.readString();
    Serial.println(dataIn);
    pos = map(findX(dataIn), 100, 400, 0, 180);
    servox.write(pos);
    //servoy.write(map(findY(dataIn), 100, 400, 0, 180)); For when i put y axis control in.
    Serial.println(abs(pos - prevpos));

    if (abs(pos - prevpos) < 5 & prevpos > 0) {
      Serial.println("pew");
    }
    prevpos = pos;
  }
}


int findX(String dataIn) {
  dataIn.remove(dataIn.indexOf("x"), 1);
  dataIn.remove(dataIn.indexOf("y"), 4);

  return dataIn.toInt();
}


int findY(String dataIn) {
  dataIn.remove(dataIn.indexOf("x"), dataIn.indexOf("y") + 1);

  return dataIn.toInt();
}

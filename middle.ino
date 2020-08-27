#include <Servo.h>
Servo servox;
Servo servoy;
String dataIn;
int xval;
int yval;

void setup() {
  // put your setup code here, to run once:
  Serial.setTimeout(10);
  Serial.begin(9600);
  servox.attach(9);
  servoy.attach(5);
  servox.write(90);
  servoy.write(90);

  //dataIn = "x198y478";

}

void loop(){
  //

}

void serialEvent(){
  dataIn = Serial.readString();
  Serial.println(dataIn);
  servox.write(map(findX, 0,500,0,180));
  servoy.write(map(findY, 0,500,0,180));
}

int findX(String dataIn){
  dataIn.remove(dataIn.indexOf("x"), 1);
  dataIn.remove(dataIn.indexOf("y"), 4);

  return dataIn.toInt();
  
}

int findY(String dataIn){
  dataIn.remove(dataIn.indexOf("x"),dataIn.indexOf("y")+1);
  
  return dataIn.toInt();
}

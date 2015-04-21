#include <Servo.h>

Servo x_axis, z_axis;
String incomingByte = "";

void setup() {
  Serial.begin(9600);
  x_axis.attach(9);
  z_axis.attach(8);
  x_axis.write(90);
  z_axis.write(90);
}


void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    int xpos = incomingByte.toInt();
    //Serial.println(xpos);
    incomingByte = Serial.readStringUntil('\n');
    int zpos = incomingByte.toInt();
    //Serial.println(zpos);
    x_axis.write(180-xpos);
    z_axis.write(180-zpos);
    delay(10);
  }
}

#include <Servo.h>

Servo x_axis, z_axis;
String incomingByte = "";

void setup() {
  Serial.begin(9600);
  x_axis.attach(A0);
  z_axis.attach(A1);
  x_axis.write(50);
  z_axis.write(0);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    int xpos = (incomingByte.substring(incomingByte.indexOf(':')+1)).toInt();
    incomingByte = Serial.readStringUntil('\n');
    int zpos = (incomingByte.substring(incomingByte.indexOf(':')+1)).toInt();
    x_axis.write(xpos);
    z_axis.write(zpos);
  }
  delay(25);
}

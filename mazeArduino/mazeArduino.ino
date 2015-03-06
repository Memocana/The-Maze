#include <Servo.h>

Servo x_axis, z_axis;
String incomingByte = "";

void setup() {
  Serial.begin(9600);
  x_axis.attach(A0);
  z_axis.attach(A1);
  x_axis.write(90);
  z_axis.write(90);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    String xpos = incomingByte.substring(incomingByte.indexOf(':')+1);
    incomingByte = Serial.readStringUntil('\n');
    String zpos = incomingByte.substring(incomingByte.indexOf(':')+1);
    x_axis.write(int(xpos));
    z_axis.write(int(zpos));
  }
  delay(25);
}

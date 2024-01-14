// Include the Servo library 
#include <Servo.h> 
// Declare the Servo pin 
int servoPin = 9; 
// Create a servo object 
Servo Servo1;
void setup() {
Servo1.attach(servoPin); 
  // put your setup code here, to run once:
Serial.begin(9600);
  // put your setup code here, to run once:
}

void loop() {
    Servo1.write(90); 
    delay(1000); 
//  // put your main code here, to run repeatedly: 
  if(Serial.available()>0)
{
  char val= Serial.read();
  if(val=='s')
  {
    Servo1.write(90); 
    delay(1000);   
   }
  if(val=='l')
  {
   Servo1.write(90); 
    delay(1000); 
   // Make servo go to 90 degrees 
   Servo1.write(30); 
    delay(1000); 
    Servo1.write(90); 
    delay(1000); 
    
   }
   if(val=='m')
  {
   Servo1.write(90); 
    delay(1000); 
   // Make servo go to 90 degrees 
   Servo1.write(0); 
    delay(1000); 
    Servo1.write(90); 
    delay(1000);   }
   if(val=='r')
  {
  Servo1.write(90); 
    delay(1000); 
   // Make servo go to 90 degrees 
   Servo1.write(150); 
    delay(1000); 
    Servo1.write(90); 
    delay(1000); 
   }
  if(val=='n')
  {
   Servo1.write(90); 
    delay(1000); 
   // Make servo go to 90 degrees 
   Servo1.write(180); 
    delay(1000); 
    Servo1.write(90); 
    delay(1000);
  }
  }
}

const int pwPin = 7;
unsigned long pulse;
unsigned int mm, inches;

#include <EnableInterrupt.h>

#define RXIN 3
#define PWM_SWITCH 5
#define receiverThrottle 1400 // us


/*
 * throttle output to common
 * normally closed remote
 * normally open RPi
 */

unsigned long startPulse;


void Switch() {
  if (digitalRead(RXIN) == HIGH) {
   startPulse = micros(); 
  }
  else {
    noInterrupts();
    int pulseLength = micros() - startPulse;
    if(pulseLength > receiverThrottle) { // RPi activated
      Serial.println("HIHG");
      digitalWrite(PWM_SWITCH, HIGH);
    }
    else {
      Serial.println("LOW");
      digitalWrite(PWM_SWITCH, LOW);
    }
  }
  interrupts();
}


void setup()

{
  Serial.begin(9600);
  pinMode(PWM_SWITCH, OUTPUT);
  pinMode(RXIN, INPUT);
  enableInterrupt(RXIN, Switch, CHANGE); // create event that calls Switch everytime the pin chagnes state
}

void loop()

{
  pinMode(pwPin, INPUT);
  
  //Used to read in the pulse that is being sent by the MaxSonar device.
  //Pulse Width representation with a scale factor of 147 uS per Inch.

  pulse = pulseIn(pwPin, HIGH);

  //147uS per inch

  inches = pulse / 147;

  //change inches to centimetres

  mm = inches * 25.4;
  Serial.println(mm);

}

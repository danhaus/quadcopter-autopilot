#include <EnableInterrupt.h>

#define RXIN 3
#define PWM_SWITCH 4
#define receiverThrottle 1500 // us

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
      digitalWrite(PWM_SWITCH, HIGH);
    }
    else {
      digitalWrite(PWM_SWITCH, LOW);
    }
  }
  interrupts();
}

void setup() {
  enableInterrupt(RXIN, Switch, CHANGE); // create event that calls Switch everytime the pin chagnes state
}

void loop() {
  
}




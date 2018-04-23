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

void setup() {
  Serial.begin(9600);
  pinMode(PWM_SWITCH, OUTPUT);
  pinMode(RXIN, INPUT);
  enableInterrupt(RXIN, Switch, CHANGE); // create event that calls Switch everytime the pin chagnes state
}

void loop() {

}




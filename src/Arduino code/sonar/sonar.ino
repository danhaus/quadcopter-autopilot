const int pwPin = 7;
long pulse, mm, inches;

void setup()

{
  Serial.begin(9600);
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

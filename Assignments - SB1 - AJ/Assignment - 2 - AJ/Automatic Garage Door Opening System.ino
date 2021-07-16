#include<Servo.h>
Servo s;
int trig = 8;
int echo = 9;

int getDist()
{
  digitalWrite(trig,LOW);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  float dur = pulseIn(echo,HIGH);
  float dis = (dur*0.034)/2;
  return dis;
}

//Open thr Door
void open()
{
  for(int i=0;i<=180;i++){
    s.write(i);
    delay(100);}
}

//Close thr Door
void close()
{
  for(int j=180;j>=0;j--){
    s.write(j);
    delay(10);
  }
}

//Initializing the Pins
void setup()
{
  s.attach(4);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int dis = getDist();
  Serial.print("Distance in cm: ");
  Serial.println(dis);
  if(dis < 50)
  {
    Serial.println("Distance is lesser than 50cm");
    Serial.println("---Opening the Garage Door---");
    open();
    Serial.println("---Waiting for 5 secs---");
    delay(5000);
    Serial.println("---Closing the Garage Door---");
    close();
  }
  else
  {
    Serial.println("Distance is greater than 50cm");
    s.write(0);
  }
  Serial.println("---Delay of 5 secs---");
  delay(5000);
}

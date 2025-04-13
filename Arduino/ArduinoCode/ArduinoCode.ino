#include <SoftwareSerial.h>

#define BT_RXD 7
#define BT_TXD 6

SoftwareSerial bluetooth(BT_TXD, BT_RXD);

#define EA 3
#define EB 11
#define M_IN1 4
#define M_IN2 5
#define M_IN3 13
#define M_IN4 12
#define R_Sensor 8
#define C_Sensor 9
#define L_Sensor 10

int motorA_vector = 1;
int motorB_vector = 1;
int motor_speed = 1023;
int intersection_count = 0;
int target_intersection = 0;
bool previous_ir_left = false;
bool activated = false;
bool is_delivered = false; 

void init_pin()
{
  pinMode(EA, OUTPUT);
  pinMode(EB, OUTPUT);
  pinMode(M_IN1, OUTPUT);
  pinMode(M_IN2, OUTPUT);
  pinMode(M_IN3, OUTPUT);
  pinMode(M_IN4, OUTPUT);
  pinMode(R_Sensor, INPUT);
  pinMode(C_Sensor, INPUT);
  pinMode(L_Sensor, INPUT);
}

void setup()
{
  bluetooth.begin(9600);
  Serial.begin(9600);
  init_pin();
  delay(3000);
}

void loop()
{
  if (!activated)
  {
    if (bluetooth.available()) {
      char cmd = bluetooth.read();
      target_intersection = cmd - '0';
      Serial.println(target_intersection);
      activated = !activated;
    }
  }
  else
  {
    if (digitalRead(C_Sensor))
    {
      motor_con(motor_speed, motor_speed);
    }
  
    if (digitalRead(L_Sensor))
    {
      if (previous_ir_left == false)
      {
        intersection_count++;
        previous_ir_left = true;
        if (intersection_count == target_intersection)
        {
          turn_left();
          delay(200);
          is_delivered=true;
          previous_ir_left = false;
        }
      }
    }
    else
    {
      previous_ir_left = false;
    }
    if (is_out_of_range())
    {
      stop_motors();
      if (is_delivered)
      {
        activated = false;
        is_delivered = false;
        intersection_count = 0;
      }
    }
  }
}

void stop_motors()
{
  motor_con(0, 0);
}

bool is_out_of_range()
{
  return digitalRead(L_Sensor) == LOW &&
         digitalRead(C_Sensor) == LOW &&
         digitalRead(R_Sensor) == LOW;
}

void turn_left()
{
  motor_con(motor_speed, -(motor_speed));
}

void turn_right()
{
  motor_con(-(motor_speed), motor_speed);
}

void motor_con(int M1, int M2)
{
  if (M1 > 0)
  {
    digitalWrite(M_IN1, motorA_vector);
    digitalWrite(M_IN2, !motorA_vector);
  }
  else if (M1 < 0)
  {
    digitalWrite(M_IN1, !motorA_vector);
    digitalWrite(M_IN2, motorA_vector);
  }
  else
  {      
    digitalWrite(M_IN1, LOW);
    digitalWrite(M_IN2, LOW);
  }

  if (M2 > 0)
  { 
    digitalWrite(M_IN3, motorB_vector);
    digitalWrite(M_IN4, !motorB_vector);
  }
  else if (M2 < 0)
  { 
    digitalWrite(M_IN3, !motorB_vector);
    digitalWrite(M_IN4, motorB_vector);
  }
  else
  {
    digitalWrite(M_IN3, LOW);
    digitalWrite(M_IN4, LOW);
  }
  
  analogWrite(EA, abs(M1));
  analogWrite(EB, abs(M2));

}
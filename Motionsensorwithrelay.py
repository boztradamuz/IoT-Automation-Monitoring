import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#MotionSensor Pin
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

#Relay Pin
RELAY_PIN=18
GPIO.setup(RELAY_PIN, GPIO.OUT)

state=0
try:
               print("Module Test (CTRL+C to exit)")
               print("Auto Light Switch with motion sensor)
               
               time.sleep(2)
               print("Ready")
               while True:
                             if GPIO.input(PIR_PIN):
                                             print ("Motion Detected!")
                                             if state==0:
                                                 state=1
                                                 GPIO.output(RELAY_PIN,GPIO.HIGH)
                                                 print(">>>>>>>>>>>>>>> State:",state,"Welcome!")
                                             else:
                                                state=0
                                                GPIO.output(RELAY_PIN,GPIO.LOW)
                                                print(">>>>>>>>>>>>>>>> State:",state,"Goodbye!")
                            
                             print ("Settle down")             
                             #time.sleep(1)
                             #print("5")
                             #time.sleep(1)
                             #print("4")
                             time.sleep(1)
                             print("3")
                             time.sleep(1)
                             print("2")
                             time.sleep(1)
                             print("1")
                             
                             
                                             
except KeyboardInterrupt:
               print (" Quit ")
               GPIO.cleanup()

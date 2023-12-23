import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setMode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50) # 50Hz 설정
pwm.start(3.0) # High 3% (0도)

for t_high in range(30, 125): # 0도->180도
    pwm.ChangeDutyCycle(t_high/10.0) # High 3.1%, 3.2%, ...
    time.sleep(0.02)

pwm.ChangeDutyCycle(3.0) # High 3% (0도)
time.sleep(1.0)
pwm.ChangeDutyCycle(0.0) # High 0%. 작동 중지

pwm.stop()
GPIO.cleanup()
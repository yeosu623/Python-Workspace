import RPi.GPIO as GPIO
import time

buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 262) # 주파수를 262Hz(도)로 설정
pwm.start(50.0) # 50%의 High를 갖도록 설정. 이 코드 이후부터 소리가 나기 시작함
time.sleep(2.0)

pwm.ChangeFrequency(294) #주파수를 294Hz(레)로 설정
time.sleep(2.0)

pwm.stop()
GPIO.cleanup()
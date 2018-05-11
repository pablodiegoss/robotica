import ev3dev.ev3 as ev3
import time


def log(motor):
    print("speed" + str(motor.speed))


m = ev3.Motor("outA")
m2 = ev3.Motor("outB")
m3 = ev3.Motor("outD")
infrared = ev3.InfraredSensor('in1')
color = ev3.ColorSensor('in2')
button = ev3.Button()
infrared.auto_mode = False
infrared.mode = infrared.MODE_IR_PROX

print("Ready!")
while True:
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  AAAAAAA")
    if button.any():
        break


time.sleep(5)

velocity = 100

m.run_direct(duty_cycle_sp=velocity)
m2.run_direct(duty_cycle_sp=velocity)
m3.run_direct(duty_cycle_sp=0)
activeMotor = m
while True:
    print("Proximity :" + str(infrared.proximity))
    if(infrared.proximity > 50):
        if(color.color == color.COLOR_BLACK):
            activeMotor.duty_cycle_sp = 100
        else:
            activeMotor.duty_cycle_sp = -100
        m3.duty_cycle_sp = 0
    else:
        if(infrared.proximity<25):
            m3.duty_cycle_sp = -100
        activeMotor.duty_cycle_sp = 100
        log(activeMotor)
    if button.any():
        break

m.stop()
m2.stop()
m3.stop()


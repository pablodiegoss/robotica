import ev3dev.ev3 as ev3

m = ev3.Motor("outA")
m2 = ev3.Motor("outB")
m.run_direct(duty_cycle_sp=100)
m2.run_direct(duty_cycle_sp=100)
infrared = ev3.InfraredSensor('in1')
button = ev3.Button()
infrared.auto_mode = False
infrared.mode = infrared.MODE_IR_PROX

while True:
    print(infrared.proximity)
    if(infrared.proximity > 50):
        m.duty_cycle_sp = -100
    else:
        m.duty_cycle_sp = 100

    if button.any():
        break

m.stop()
m2.stop()

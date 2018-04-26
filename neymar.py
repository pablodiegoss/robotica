import ev3dev.ev3 as ev3

m = ev3.Motor("outA")
m2 = ev3.Motor("outB")
m.run_direct(speed_sp=1000, duty_cycle_sp=100)
m2.run_direct(speed_sp=1000, duty_cycle_sp=100)
infrared = ev3.InfraredSensor('in3')
infrared.MODE_IR_PROX
button = ev3.Button()

infrared_old = 100
infrared_mean = 100
COUNT = 5
proximity_sum = 0
variable = 0
while True:
    if(infrared_old > 50):
        m.duty_cycle_sp = -100
    else:
        m.duty_cycle_sp = 100

    if(infrared_mean != infrared_old):
        print(infrared_mean)
        infrared_old = infrared_mean

    proximity_sum += infrared.proximity
    variable+=1

    if(variable > COUNT):
        infrared_mean = proximity_sum/variable
        proximity_sum = 0
        variable = 0

    if button.any():
        break


m.stop()
m2.stop()

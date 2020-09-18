import odrive

#1

odrv0.erase_configuration()
odrv0.reboot()



#2
pole_pairs = 11

kv = 620

cpr = 8192

voltage = 12 




odrv0.axis0.motor.config.current_lim = 20
odrv0.axis0.controller.config.vel_limit = .75 * cpr * voltage * kv 
odrv0.config.brake_resistance = .05
odrv0.axis0.motor.config.pole_pairs = pole_pairs
odrv0.axis0.motor.config.motor_type = MOTOR_TYPE_HIGH_CURRENT

odrv0.axis0.encoder.config.cpr = cpr


odrv0.save_configuration() 
odrv0.reboot()

#3

odrv0.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

#4

odrv0.axis0.controller.config.vel_integrator_gain = 0 
odrv0.axis0.controller.config.vel_gain = .00025
odrv0.axis0.controller.config.pos_gain = 20
odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL


#5

start_liveplotter(lambda:[odrv0.axis0.encoder.pos_estimate, odrv0.axis0.controller.pos_setpoint])

odrv0.axis0.controller.pos_setpoint


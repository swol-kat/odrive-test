import odrive

#1


odrv0.erase_configuration()
try:    
    odrv0.reboot()
except:
    print('reboot')



#2
pole_pairs = 20

kv = 160

cpr = 2048

voltage = 12 




odrv0.axis0.motor.config.current_lim = 20
odrv0.axis0.controller.config.vel_limit = .75 * cpr * voltage * kv 
odrv0.config.brake_resistance = .05
odrv0.axis0.motor.config.pole_pairs = pole_pairs
odrv0.axis0.motor.config.motor_type = MOTOR_TYPE_HIGH_CURRENT
odrv0.axis0.motor.config.calibration_current = 10.0 



odrv0.axis0.encoder.config.cpr = cpr
odrv0.axis0.encoder.config.mode = ENCODER_MODE_INCREMENTAL
odrv0.axis0.encoder.config.calib_range = 0.05 



odrv0.save_configuration() 
try:    
    odrv0.reboot()
except:
    print('reboot')

#3

odrv0.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

#4

odrv0.axis0.controller.config.vel_integrator_gain = 0 
odrv0.axis0.controller.config.vel_gain = .0035
odrv0.axis0.controller.config.pos_gain = 30
odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

odrv0.axis0.controller.pos_setpoint = odrv0.axis0.controller.pos_setpoint + 1*cpr

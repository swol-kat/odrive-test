# import odrive

#1


odrv0.erase_configuration()



#2
pole_pairs = 20

kv = 160

cpr = 16384

voltage = odrv0.vbus_voltage 




odrv0.axis0.motor.config.current_lim= 20.0
odrv0.axis0.controller.config.vel_limit = .75  * voltage * kv /60
odrv0.config.brake_resistance = .05
odrv0.axis0.motor.config.pole_pairs = pole_pairs
odrv0.axis0.motor.config.torque_constant = 8.27 / kv
odrv0.axis0.motor.config.motor_type = MOTOR_TYPE_HIGH_CURRENT

odrv0.axis0.encoder.config.abs_spi_cs_gpio_pin = 4  # or which ever GPIO pin you choose
odrv0.axis0.encoder.config.mode = ENCODER_MODE_SPI_ABS_AMS   # or ENCODER_MODE_SPI_ABS_AMS
odrv0.axis0.encoder.config.cpr = cpr           

odrv0.axis0.controller.config.pos_gain = 20
odrv0.axis0.controller.config.vel_gain = .01
odrv0.axis0.controller.config.vel_integrator_gain = .01



odrv0.save_configuration() 
odrv0.reboot()
#3

odrv0.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE

#4


# odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# # #veloctiy control
# # odrv0.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL

# # odrv0.axis0.controller.input_vel = 1 

# # current control
# odrv0.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL

# odrv0.axis0.controller.input_torque = 0.1


# #5
# odrv0.axis0.controller.input_pos = 1
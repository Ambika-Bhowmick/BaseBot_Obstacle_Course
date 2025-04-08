# This is the code for the obstacle course
# Begin project code
drivetrain.set_drive_velocity(75, PERCENT)
drivetrain.drive_for(FORWARD, 440, MM)
#These are the cones
drivetrain.drive_for(FORWARD, 70, MM)
drivetrain.drive_for(RIGHT,15, DEGREES)
drivetrain.drive_for(FORWARD, 20, MM)
drivetrain.drive_for(LEFT, 15, DEGREES)
drivetrain.drive_for(FORWARD, 250, MM)
# This is for going to the walls and turning for the walls
drivetrain.drive_for(FORWARD, 360, MM)
drivetrain.drive_for(RIGHT 90, DEGREES)
drivetrain.drive_for(FORWARD, 210, MM)
drivetrain.drive_for(RIGHT 90, DEGREES)
# This is the tunnel
drivetrain.drive_for(FORWARD, 210, MM)
# This is the seesaw
drivetrain.set_drive_velocity(50, PERCENT)
drivetrain.drive_for(FORWARD, 440, MM)
drivetrain.drive_for(RIGHT 90, DEGREES)
# This is for the ending ramp
drivetrain.set_drive_velocity(75, PERCENT)
drivetrain.drive_for(FORWARD, 440, MM)
# This is the end
drivetrain.set_stopping(BRAKE)

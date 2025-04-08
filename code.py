# This is the code for the obstacle course
# Begin project code
drivetrain.set_drive_velocity(75, PERCENT)
drivetrain.drive_for(FORWARD, 600, MM)
# This is the code for the cones
drivetrain.drive_for(FORWARD, 180, MM)
drivetrain.drive_for(LEFT, 47, DEGREES)
drivetrain.drive_for(FORWARD, 25, MM)
drivetrain.drive_for(RIGHT 94, DEGREES)
drivetrain.drive_for(FORWARD, 25, MM)
drivetrain.drive_for(LEFT, 47, DEGREES)
drivetrain.drive_for(FORWARD, 25, MM)
drivetrain.drive_for(RIGHT 47, DEGREES)
# This is for going to the walls and turning for the walls
drivetrain.drive_for(FORWARD, 250, MM)
drivetrain.drive_for(RIGHT 90, DEGREES)
drivetrain.drive_for(FORWARD, 500, MM)
drivetrain.drive_for(RIGHT 90, DEGREES)
#These are the second cones
drivetrain.drive_for(FORWARD, 40, MM)
drivetrain.drive_for(LEFT, 47, DEGREES)
drivetrain.drive_for(FORWARD, 25 MM)
drivetrain.drive_for(RIGHT 94, DEGREES)
drivetrain.drive_for(FORWARD, 25 MM)
drivetrain.drive_for(LEFT, 47, DEGREES)
# This is the tunnel
drivetrain.drive_for(FORWARD, 250, MM)
drivetrain.drive_for(RIGHT 90, DEGREES)
# This is the seesaw
drivetrain.set_drive_velocity(50, PERCENT)
drivetrain.drive_for(FORWARD, 380, MM)
# This is for the ending ramp
drivetrain.set_drive_velocity(75, PERCENT)
drivetrain.drive_for(FORWARD, 150, MM)
# This is the end
drivetrain.set_stopping(BRAKE)





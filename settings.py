from math import sqrt


# D-pad
D_SIZE = (55, 55)
D_ALPHA = 0.2

## Player
# Speed
MAX_SPEED = 5
MAX_SPEED_D = sqrt((MAX_SPEED**2)/2)

ACC = 0.05
MAX_ACC = 1

FRICTION = -0.05

ROT_TIME = 5

## Bullet
# Speed
BULLET_SPEED = 10
SHOOT_RATE = 10  # miliseconds between shots

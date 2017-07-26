from math import sqrt


## D-pad
#D_SIZE = (100, 100) #(55, 55)
D_ALPHA = 0.2


## Player
MAX_SPEED = 5
MAX_SPEED_D = sqrt((MAX_SPEED**2)/2)

ACC = 0.05
MAX_ACC = 1

FRICTION = -0.05

ROT_TIME = 5

MAX_HEALTH = 100
MAX_ENERGY = 100

BAR_DIST = 185
BAR_HEIGHT = 5
DEP_TIME = 360 # Depletion rate in miliseconds

HF_COL = '#ff0000'
HB_COL = '#810000'

EF_COL = '#0098ff'
EB_COL = '#004c80'

## Bullet
BULLET_SPEED = 5
SHOOT_RATE = 10  # miliseconds between shots
BULLET_COL = '#f3ff00'
BULLET_DAMG = 10

from math import sqrt


## D-pad
#D_SIZE = (100, 100) #(55, 55)
D_ALPHA = 0.2


## Player
SHOW_HITBOX = True

P1_COL = '#0000ff'
P2_COL = '#ff0000'

MAX_SPEED = 5
MAX_SPEED_D = sqrt((MAX_SPEED**2)/2)

ACC = 0.05
MAX_ACC = 1

FRICTION = -0.05

ROT_TIME = 5

MAX_HEALTH = 100
MAX_ENERGY = 100
ENERGY_REGEN = 0.5


## Resource Bars
BAR_DIST = 185
BAR_HEIGHT = 5

HF_COL = '#ff0000'  # Health bar (fore)
HB_COL = '#810000'  # Health bar (back)

EF_COL = '#0098ff'  # Energy bar (fore)
EB_COL = '#004c80'  # Energy bar (back)


## Bullet
BULLET_SPEED = 10
SHOOT_RATE = 10  # miliseconds between shots
BULLET_COL = '#f3ff00'
BULLET_DAMG = 20
BULLET_DEP = 10


## Effects
FX_DESPAWN = 200  # In miliseconds

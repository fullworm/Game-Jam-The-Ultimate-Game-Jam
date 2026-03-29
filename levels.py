import pygame, Room, entities
from constants import *

# ============================== LEVEL 1 ==============================
#         Exit
# left    Start   Right
#         Down

lvl1Start = Room.Room(
    {"Up": "Exit",
     "Down": "Down",
     "Left": "Left",
     "Right": "Right"},

    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]],

    None,

    (int(5.5 * TILESIZE), int(5.5 * TILESIZE)),
    terminal=entities.Terminal(6 * TILESIZE, TILESIZE, PLAYERSIZE, PLAYERSIZE)
)
lvl1Left = Room.Room(
    {"Up": None,
     "Down": None,
     "Left": None,
     "Right": "Start"},

    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

    [entities.Enemy(3 * TILESIZE, 3 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False),
     entities.Enemy(3 * TILESIZE, 8 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False),
     entities.Enemy(6.5 * TILESIZE, 5.5 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False),],

    (int(9.5 * TILESIZE), int(5.5 * TILESIZE)),
    collectable=entities.Message(2 * TILESIZE, 6 * TILESIZE, 20, 20, "so prety")
)
lvl1Right = Room.Room(
    {"Up": None,
     "Down": None,
     "Left": "Start",
     "Right": None},

    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

    [entities.Enemy(4 * TILESIZE, 1 * TILESIZE, TILESIZE, 10 * TILESIZE, False, 1),
     entities.Enemy(7 * TILESIZE, 1 * TILESIZE, TILESIZE, 10 * TILESIZE, False, 1),],

    (int(2.5 * TILESIZE), int(5.5 * TILESIZE)), 
    collectable=entities.Message(10 * TILESIZE, 6 * TILESIZE, 20, 20, "ultimate rizz")

)
lvl1Down = Room.Room(
    {"Up": "Start",
     "Down": None,
     "Left": None,
     "Right": None},

    [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

    [entities.Enemy(2 * TILESIZE, 4 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, True, False),
     entities.Enemy(9 * TILESIZE, 6 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False),
     entities.Enemy(2 * TILESIZE, 8 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, True, False),],

    (int(5.5 * TILESIZE), int(2.5 * TILESIZE)),
    collectable=entities.Message(6 * TILESIZE, 10 * TILESIZE, 20, 20, "-30 aura")

)
lvl1Exit = Room.Room(
    {"Up": None,
     "Down": "Start",
     "Left": None,
     "Right": None},

    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]],

    None,

    None
)
lvl1 = {"Start": lvl1Start,
        "Left": lvl1Left,
        "Right": lvl1Right,
        "Down": lvl1Down,
        "Exit": lvl1Exit}

# ============================== LEVEL 2 ==============================

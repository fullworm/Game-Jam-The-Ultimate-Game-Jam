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
    terminal=entities.Terminal(5.5 * TILESIZE, 2* TILESIZE, TILESIZE, TILESIZE, False),
    boy=True
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

    [entities.Enemy(3 * TILESIZE, 3 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves=True, speed=1),
     entities.Enemy(3 * TILESIZE, 8 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves=True, speed=1),
     entities.Enemy(6.5 * TILESIZE, 5.5 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves=True, speed=1),],

    (int(9.5 * TILESIZE), int(5.5 * TILESIZE)),
    collectable=entities.Message(2 * TILESIZE, 5.5 * TILESIZE, PLAYERSIZE, PLAYERSIZE, "*Hey... We've known each other for some time*", True, id=2),
    boy=True
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

    [entities.Enemy(4 * TILESIZE, 1 * TILESIZE, TILESIZE, 10 * TILESIZE, False, 1, laser=1),
     entities.Enemy(7 * TILESIZE, 1 * TILESIZE, TILESIZE, 10 * TILESIZE, False, 1, laser=1),],

    (int(2.5 * TILESIZE), int(5.5 * TILESIZE)), 
    collectable=entities.Message(10 * TILESIZE, 5.5 * TILESIZE, PLAYERSIZE, PLAYERSIZE, "*Would you like to go on a date with me?*", True, id=5),
    boy=True
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
    collectable=entities.Message(5.5 * TILESIZE, 10 * TILESIZE, PLAYERSIZE, PLAYERSIZE, "*I've been afraid to ask...*", True, id=3),
    boy=True

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

    None,
    boy=True

)
lvl1 = {"Start": lvl1Start,
        "Left": lvl1Left,
        "Right": lvl1Right,
        "Down": lvl1Down,
        "Exit": lvl1Exit}

# ============================== LEVEL 2 ==============================
lvl2Start = Room.Room(
    {"Up": None,
     "Down": None,
     "Left": None,
     "Right": "Right"},

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

    None,

    (int(5.5 * TILESIZE), int(5.5 * TILESIZE)),
    terminal=entities.Terminal(5.5 * TILESIZE, 2.5*TILESIZE, TILESIZE, TILESIZE, True),
    boy=False

)
lvl2Left = Room.Room(
    {"Up": "Down",
     "Down": None,
     "Left": "Right",
     "Right": None},

    [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
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

    [entities.Enemy(10 * TILESIZE,  TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, shoots=True),
     entities.Enemy(10 * TILESIZE, 10* TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, shoots=True),
     entities.Enemy(8 * TILESIZE, 5.5 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves=True, speed=1.5),],

    (int(2.5* TILESIZE), int(5.5 * TILESIZE)),
    collectable=entities.Message(5.5 * TILESIZE, 5.5 * TILESIZE, 20, 20, "*What kind of question is that??*", False, id=3),
    boy=False

)
lvl2Right = Room.Room(
    {"Up": None,
        "Down": None,
        "Left": "Start", 
        "Right": "Left"},

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
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

    [entities.Enemy(3 * TILESIZE, 3 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True,random_m=True, speed=2),
     entities.Enemy(3 * TILESIZE, 8 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True,random_m=True, speed=2),
     entities.Enemy(6.5 * TILESIZE, 5.5 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True, random_m=True, speed=2)],

    (int(2.5*TILESIZE), int(5.5 * TILESIZE)),
    collectable=entities.Message(5.5 * TILESIZE, 9.5 * TILESIZE, 20, 20, "*Me? on a date with you?*", False, id=2),
    boy=False

)
lvl2Down = Room.Room(
    {"Up": None,
     "Down": "Left",
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

    [entities.Enemy(2* TILESIZE,  2*TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, True, False, shoots=True),
     entities.Enemy(5.5 * TILESIZE, 5.5 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves=True, random_m=True, shoots=True, speed=1.6),
     entities.Enemy(8 * TILESIZE,  2*TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, True, False, shoots=True),],

    (int(5.5 * TILESIZE), int(9.5 * TILESIZE)),
    collectable=entities.Message(5.5 * TILESIZE, 2.5 * TILESIZE, 20, 20, "*Of course I would love to! <3*", False, id=5),
    boy=False

)
lvl2Exit = Room.Room(
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

    None,
    boy=False

)
lvl2 = {"Start": lvl2Start,
        "Left": lvl2Left,
        "Right": lvl2Right,
        "Down": lvl2Down,
        "Exit": lvl2Exit}

# ============================Level 3====================

lvl3Start = Room.Room(
    {"Up": None,
     "Down": "Right",
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

    (int(5.5 * TILESIZE), int(5.5 * TILESIZE)),
    terminal=entities.Terminal(5.5 * TILESIZE, 2.5*TILESIZE, TILESIZE, TILESIZE, False),
    boy=True

)
lvl3Left = Room.Room(
    {"Up": None,
     "Down": "Down",
     "Left": "Right",
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
     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]],

    [entities.Enemy(TILESIZE, TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True, shoots=True, speed=2, random_m=True),
     entities.Enemy(5.5 * TILESIZE, 5.5 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True, shoots=True, speed=2, random_m=True),
     entities.Enemy( TILESIZE, 10 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True, shoots=True, speed=2, random_m=True),
     entities.Enemy(10 * TILESIZE,  TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True, shoots=True, speed=2, random_m=True),
     entities.Enemy(10* TILESIZE, 10 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True, shoots=True, speed=2, random_m=True)],

    (int(TILESIZE), int(5.5 * TILESIZE)),
    collectable=entities.Message(9.5 * TILESIZE, 2.5 * TILESIZE, 20, 20, "*Then... let's connect tomorrow, deal?*", True, id=3),
    boy=True

)
lvl3Right = Room.Room(
    {"Up": "Start",
        "Down": None,
        "Left": None, 
        "Right": "Left"},

    [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
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

    [entities.Turret(5.5 * TILESIZE, 5.5 * TILESIZE)],

    (int(5.5 * TILESIZE), int(TILESIZE)),
    collectable=entities.Message(2.5 * TILESIZE, 9.5 * TILESIZE, 20, 20, "*Wait, you do?*", True, id=2),
    boy=True

)
lvl3Down = Room.Room(
    {"Up": "Left",
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

    [entities.Enemy( TILESIZE, 3 * TILESIZE, 10* TILESIZE, TILESIZE, moving_right=False, moving_down=1, laser=2),
     entities.Enemy( TILESIZE, 7 * TILESIZE, 10* TILESIZE, TILESIZE, moving_right=False, moving_down=1, laser=2),
     entities.Enemy(5.5 * TILESIZE, 5.5 * TILESIZE, BASICENEMYSIZE, BASICENEMYSIZE, False, False, moves= True, shoots=True, speed=2, random_m=True),],

    (int(5.5 * TILESIZE), int(TILESIZE)),
    collectable=entities.Message(5.5 * TILESIZE, 9.5 * TILESIZE, 20, 20, "*See you then!*", True, id=5),
    boy=True

)
lvl3Exit = Room.Room(
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

    None,
    boy = True

)
lvl3 = {"Start": lvl3Start,
        "Left": lvl3Left,
        "Right": lvl3Right,
        "Down": lvl3Down,
        "Exit": lvl3Exit}
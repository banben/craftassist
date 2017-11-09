from typing import Dict, Callable

import shapes

# mapping from mob names to id
SPAWN_OBJECTS = {
    "elder guardian": 4,
    "wither skeleton": 5,
    "stray": 6,
    "husk": 23,
    "zombie villager": 27,
    "skeleton horse": 28,
    "zombie horse": 29,
    "donkey": 31,
    "mule": 32,
    "evoker": 34,
    "vex": 35,
    "vindicator": 36,
    "creeper": 50,
    "skeleton": 51,
    "spider": 52,
    "zombie": 54,
    "slime": 55,
    "ghast": 56,
    "zombie pigman": 57,
    "enderman": 58,
    "cave spider": 59,
    "silverfish": 60,
    "blaze": 61,
    "magma cube": 62,
    "bat": 65,
    "witch": 66,
    "endermite": 67,
    "guardian": 68,
    "shulker": 69,
    "pig": 90,
    "sheep": 91,
    "cow": 92,
    "chicken": 93,
    "squid": 94,
    "wolf": 95,
    "mooshroom": 96,
    "ocelot": 98,
    "horse": 100,
    "rabbit": 101,
    "polar bear": 102,
    "llama": 103,
    "parrot": 105,
    "villager": 120,
}

# mapping from canonicalized shape names to the corresponding functions
SPECIAL_SHAPE_FNS: Dict[str, Callable] = {
    "CUBE": shapes.cube,
    "HOLLOW_CUBE": shapes.hollow_cube,
    "RECTANGULOID": shapes.rectanguloid,
    "HOLLOW_RECTANGULOID": shapes.hollow_rectanguloid,
    "SPHERE": shapes.sphere,
    "SPHERICAL_SHELL": shapes.spherical_shell,
    "PYRAMID": shapes.square_pyramid,
    "SQUARE": shapes.square,
    "RECTANGLE": shapes.rectangle,
    "CIRCLE": shapes.circle,
    "DISK": shapes.disk,
    "TRIANGLE": shapes.triangle,
    "DOME": shapes.dome,
    "ARCH": shapes.arch,
    "ELLIPSOID": shapes.ellipsoid,
    "TOWER": shapes.tower,
}

# mapping from shape names to canonicalized shape names
SPECIAL_SHAPES_CANONICALIZE = {
    "rectanguloid": "RECTANGULOID",
    "box": "HOLLOW_RECTANGULOID",
    "empty box": "HOLLOW_RECTANGULOID",
    "hollow box": "HOLLOW_RECTANGULOID",
    "hollow rectanguloid": "HOLLOW_RECTANGULOID",
    "cube": "CUBE",
    "empty cube": "HOLLOW_CUBE",
    "hollow cube": "HOLLOW_CUBE",
    "ball": "SPHERE",
    "sphere": "SPHERE",
    "spherical shell": "SPHERICAL_SHELL",
    "empty sphere": "SPHERICAL_SHELL",
    "empty ball": "SPHERICAL_SHELL",
    "hollow sphere": "SPHERICAL_SHELL",
    "hollow ball": "SPHERICAL_SHELL",
    "pyramid": "PYRAMID",
    "rectangle": "RECTANGLE",
    "wall": "RECTANGLE",
    "slab": "RECTANGLE",
    "platform": "RECTANGLE",
    "square": "SQUARE",
    "flat wedge": "TRIANGLE",
    "triangle": "TRIANGLE",
    "circle": "CIRCLE",
    "disk": "DISK",
    "ellipsoid": "ELLIPSOID",
    "dome": "DOME",
    "arch": "ARCH",
    "archway": "ARCH",
    "stack": "TOWER",
    "tower": "TOWER",
}

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.ClashNotRoyal
collection = db.monsters

collection.drop()

collection.insert_many([
    {
        "name": "Gobelin",
        "attack": 10,
        "defense": 5,
        "health": 50
    },
    {
        "name": "Géant",
        "attack": 20,
        "defense": 8,
        "health": 120
    },
    {
        "name": "Dragon de l'enfer",
        "attack": 35,
        "defense": 20,
        "health": 300
    },
    {
        "name": "Cochon royal",
        "attack": 12,
        "defense": 6,
        "health": 70
    },
    {
        "name": "Fantôme royal",
        "attack": 25,
        "defense": 15,
        "health": 200
    },
    {
        "name": "Barbare",
        "attack": 18,
        "defense": 10,
        "health": 100
    },
    {
        "name": "Golem",
        "attack": 30,
        "defense": 25,
        "health": 250
    },
    {
        "name": "Sorcière",
        "attack": 22,
        "defense": 12,
        "health": 150
    },
    {
        "name": "Mega Chevalier",
        "attack": 32,
        "defense": 18,
        "health": 200
    },
    {
        "name": "Squelette",
        "attack": 15,
        "defense": 7,
        "health": 90
    }
])

collection = db.heros

collection.drop()

collection.insert_many([
    {
        "name": "Chevalier",
        "attack": 15,
        "defense": 10,
        "health": 100,
        "type": "tank",
        "effect_chance": 0.25,
        "effect_damage": 5,
        "effect_duration": 2
    },
    {
        "name": "Sorcier",
        "attack": 20,
        "defense": 5,
        "health": 80,
        "type": "sorcerer",
        "effect_chance": 0.3,
        "effect_damage": 4,
        "effect_duration": 3
    },
    {
        "name": "Archères",
        "attack": 18,
        "defense": 7,
        "health": 90,
        "type": "dps"
    },
    {
        "name": "Cheffe des voleuses",
        "attack": 22,
        "defense": 10,
        "health": 100,
        "type": "dps"
    },
    {
        "name": "Moine",
        "attack": 14,
        "defense": 12,
        "health": 110,
        "type": "tank",
        "effect_chance": 0.2,
        "effect_damage": 6,
        "effect_duration": 2
    },
    {
        "name": "Bucheron",
        "attack": 25,
        "defense": 3,
        "health": 70,
        "type": "dps"
    },
    {
        "name": "Voleur",
        "attack": 17,
        "defense": 15,
        "health": 120,
        "type": "tank",
        "effect_chance": 0.25,
        "effect_damage": 5,
        "effect_duration": 2
    },
    {
        "name": "P.E.K.K.A",
        "attack": 19,
        "defense": 9,
        "health": 95,
        "type": "dps"
    },
    {
        "name": "Chevaucheur de cochons",
        "attack": 23,
        "defense": 6,
        "health": 105,
        "type": "dps"
    },
    {
        "name": "Molosse de lave",
        "attack": 16,
        "defense": 11,
        "health": 100,
        "type": "dps"
    }
])
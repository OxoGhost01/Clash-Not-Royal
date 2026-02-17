from pymongo import MongoClient
import random

client = MongoClient('mongodb://localhost:27017/')
db = client.ClashNotRoyal

def verify_player_input(payload: str, min: int, max: int):
    player_input = input(payload)
    while True:
        try:
            if min <= int(player_input) <= max:
                return int(player_input)
            else:
                raise ValueError
        except ValueError:
            print("Nah seriously ?")
            player_input = input(payload)

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def verify_player_name():
    player_name = input("Please enter your name (3-20 characters): ")
    while True:
        if 3 <= len(player_name) <= 20:
            return player_name
        else:
            player_name = input("PLEASE enter a VALID name (is it THAT hard really?): ")

def get_all_heros():
    return db.heros.find()

def pick_monster():
    return db.monsters.aggregate([{"$sample": {"size": 1}}]).next()

def update_leaderboard(player):
    if db.players.find_one({"name": player.name}):
        db.players.update_one({"name": player.name}, {"$inc": {"score": player.score}})
    else:
        db.players.insert_one({"name": player.name, "score": player.score})

def get_loot():
    return db.loot.aggregate([{"$sample": {"size": 1}}]).next()
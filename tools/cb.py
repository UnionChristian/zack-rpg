import json
import tools.dice as dice 

def get_weapon():
    with open("data/weapons.json") as wfile:
        weapons = json.load(wfile)
    wnames = list(weapons.keys())
    wpows = list(weapons.values())
    wcount = len(wnames)
    wrand = random.randrange(1,wcount)

    weapon = {wnames[wrand]:wpows[wrand]}
    return weapon
def build(name):
    output = {
        "name": name,
        "job": "assassin",
        "strength": dice.roll(1000),
        "charisma": dice.roll(1000),
        "intelligence": dice.roll(1000),
        "luck": dice.roll(1000),
        "dexterity": dice.roll(1000),
        "weapon": dice.roll(1000),
        "constitution": dice.roll(1000),
    }
    jsonoutput = json.dumps(output)
    
    with open("data/" + name + ".json", "w") as jsonfile:
        jsonfile.write(jsonoutput)
        print("success")


build("sleepz")

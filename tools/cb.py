import json
import dice

def get_weapon():
    with open("dara/weapons.json") as wfile:
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
        "strength": dice.roll(999),
        "charisma": dice.roll(999),
        "intelligence": dice.roll(999),
        "luck": dice.roll(999),
        "dexterity": dice.roll(999),
        "weapon": dice.roll(999),
        "constitution": dice.roll(999),
    }
    jsonoutput = json.dumps(output)
    
    with open("data/" + name + "json", "w") as jsonfile:
        jsonfile.write(jsonoutput)
        print("success")


build("sleepz")

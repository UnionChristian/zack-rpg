import json
import tools.cb as cb 
import battle.hit as hit
name = input("what is your name")
cb.build(name)
hero = ""
with open("data/"+name+".json") as cfile:
    hero = json.load(cfile)
print("You are in a world that is ruled by prestige and bounty. whoever has the highest bounty and prestige is the highest shall rule the world.")
print("There are those who believe in the late kings word called hunters and are trying to achieve the highest rank so that when the end of days come they stand on top.")
print("There are also those who oppose the kings word called marines and try to get rid of all the people making trouble in the world.")
print("You are on a journey to find out the world secrets and become the new king of the world and the best hunter who ever lived.")
print("you are wondering where to go to first in your adventure")
place = input
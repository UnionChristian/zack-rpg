import json
import tools.cb as cb 
name = input("what is you name")
cb.build(name)
hero = ""
with open("data/"+name+".json") as cfile:
    hero = json.load(cfile)
print("You are in a world that is ruled by prestige and bounty. whoever has the highest bounty and prestige is the highest shall rule the world.")
print("There are those you believe in the late kings word and are trying to achieve the highest rank so that when the end of days come they stand on top.")
print("There are also those who oppose the kings word and try to get rid of all the people making trouble in the world.")
print("You are on a journey to find out the world secrets and become the new king of the world.")
print("you are wondering where to go to first in your adventure")
place = input("where do you go,do you 1. go to Alabasta 2. go to Skypia 3. go to Water 7")
if place == "1":
    print("you chose Alabasta")
    decision = input("you encounter a desert island do you 1.explore around and have fun 2. investigate for strong people with high bounties ")
    if decision == "1":
        print("you have gone to Alabasta to have fun and explore")
        decision = input("")


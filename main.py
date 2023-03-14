import json
import tools.cb as cb 
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
place = input("where do you go do you 1. go to Alabasta 2. go to Skypia 3. go to Water 7")
if place == "1":
    print("you chose Alabasta")
    decision = input("you encounter a desert island do you 1.explore around and have fun 2. investigate for strong people with high bounties ")
    if decision == "1":
        print("you have gone to Alabasta to have fun and explore")
        decision = input("you have entered the abandoned city of Yuba do you 1. move on to next city after finding nothing there 2. invistigate the city about how it came to ruins and destroyed")
        if decision == "1":
            print("you leave Yuba and head to Rainbase the home of Crocodile a very famous and strong hunter")
            decision = input("you arrive there and start looking around ")



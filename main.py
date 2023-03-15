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
place = input("where do you go do you 1. go to Alabasta 2. stay in bed and dont become a king")
if place == "2":
    print("you dont decide to become the king of the world and live a normal life at home at the mercy of the future king of the world")
if place == "1":
    print("you chose Alabasta")
    decision = input("you encounter a desert island do you 1.explore around and have fun 2. investigate for strong people with high bounties ")
    if decision == "2":
        print("you enter the desert island looking for people with high bounties")
        decision = input("you have entered the port town Nanohana known for its trading ")
    if decision == "1":
        print("you have gone to Alabasta to have fun and explore")
        decision = input("you have entered the abandoned city of Yuba do you 1. move on to next city after finding nothing there 2. invistigate the city about how it came to ruins and destroyed")
        if decision == "1":
            print("you leave Yuba and head to Rainbase the home of Crocodile a very famous and strong hunter")
            decision = input("you arrive there and start looking around for fun things to do and you see a huge gold pyramid 1. enter the pyramid 2. dont enter and look for other things")
            if decision == "1":
                print("you cross the birdge and enter the golden pyramid")
                decision = input("inside is a huge casino with penthouses named Rain Dinners owned by Crocodile do you 1. start gambling your money 2. look around the casino")
                if decision == "1":
                    print("you have started gambling all your money and you lose a lot and have become broke")
                    decision = input("you dont know what to do now that you have no more money 1. steal money from Rain Dinners and escape to the next island Skypiea 2. stay in Alabasta and try to get more money through bounty hunting ")
                    if decision == "1":
                        print("you steal money from the casino and escape to Skypiea. you currently have a bounty of 0 and have enemies chasing you from Alabasta")




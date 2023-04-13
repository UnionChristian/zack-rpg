import tools.dice as dice 
def charm(hc, ei):
    roll= dice.roll(20,1)
    cth= hc+roll
    if(cth >= ei):
        return True 
    else:
        return False 
# GET CLOCK FOR GUi
import time
import datetime as dt

class timeIs():
  
    def __init__(self):
        pass
        

    def getTime(self):

        currTime = time.localtime()
        print("the time is: \n") 
        print(currTime)
        return currTime

def main():
    

    theTime = timeIs()
    theTime.getTime()
    
    # <TODO>
    # CLEAN UP THE OUTPUT FOR THE TIME
    # TO AN EASILY READABLE FORMAT







if __name__ == "__main__":
    main()

     

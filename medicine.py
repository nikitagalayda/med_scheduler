import random

class Medicine():
    def __init__(self, name, minTime, maxTime, timeSinceDose, intervalsTaken, preferredTake):
        self.name = name
        self.minTime = minTime
        self.maxTime = maxTime
        self.timeSinceDose = timeSinceDose
        self.intervalsTaken = intervalsTaken
        self.preferredTake = preferredTake
    
    def getTimeInterval(self, daily, time):
        for i in range(len(daily)):
            time = time % 288
            if(time < daily[i][0]):
                return daily[i-1]

    def updateTime(self):
        self.timeSinceDose += 1
    
    def minTimePassed(self):
        if self.timeSinceDose >= self.minTime:
            return True
        return False

    def takeMedicine(self):
        self.timeSinceDose = 0
        self.preferredTake = -1

    def checkAhead(self, currentTime, daily):
        currentTime %= 288
        currentInterval = self.getTimeInterval(daily, currentTime)
        timeBuffer = self.maxTime - self.minTime
        
        if(currentInterval == 0):
            return

        for i in range(timeBuffer):
            aheadTime = currentTime + i
            aheadInterval = self.getTimeInterval(daily, aheadTime)
            if(currentInterval == 2):
                if(aheadInterval == 1):
                    self.preferredTake = aheadTime
            if(aheadInterval == 0):
                self.preferredTake = aheadTime
                break






# ---------ERROR CALCULATION---------
    def isTaken(self, tfType):
        if(tfType == 0):
            return True
        elif(tfType == 1):
            if random.uniform(0, 1)*10 <= 8:
                return True
        elif(tfType == 2):
            if random.uniform(0, 1)*10 <= 2:
                return True
        return False

    def calculateErrorRate(self):
        taken = []
        for i in self.intervalsTaken:
            taken.append(self.isTaken(i))
        actualTaken = 0
        # print(taken)
        for i in taken:
            if i == True:
                actualTaken += 1
        
        return actualTaken / len(taken)
        
    
    
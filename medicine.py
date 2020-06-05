import random

class Medicine():
    def __init__(self, name, minTime, maxTime, timeSinceDose, intervalsTaken, preferredTake):
        self.name = name
        self.minTime = minTime
        self.maxTime = maxTime
        self.timeSinceDose = timeSinceDose
        self.intervalsTaken = intervalsTaken
        self.preferredTake = preferredTake
        self.moveAhead = None
    
    def getTimeInterval(self, daily, time):
        for i in range(len(daily)):
            time = time % 288
            if(time < daily[i][0]):
                return daily[i-1][1]

    def updateTime(self):
        self.timeSinceDose += 1
    
    def minTimePassed(self):
        if self.timeSinceDose >= self.minTime:
            return True
        return False
    
    def atMaxTime(self):
        if self.timeSinceDose == self.maxTime:
            return True
        return False

    def takeMedicine(self):
        self.timeSinceDose = 0
        self.preferredTake = -1

    def checkAhead(self, currentTime, daily):
        # localTime = currentTime % 288
        # self.preferredTake = -1
        currentInterval = self.getTimeInterval(daily, currentTime)
        timeBuffer = self.maxTime - self.minTime
        
        if(self.preferredTake >= 0):
            return

        if(currentInterval == 0):
            return

        for i in range(timeBuffer):
            aheadTime = currentTime + i
            aheadInterval = self.getTimeInterval(daily, aheadTime)
            if(currentInterval == 2):
                # self.moveAhead = self.shiftAhead(currentTime, daily)
                if(aheadInterval == 1):
                    self.preferredTake = aheadTime
                if(aheadInterval == 0):
                    self.preferredTake = aheadTime
                    return
            if(aheadInterval == 0):
                self.preferredTake = aheadTime
                return

        # self.moveAhead = self.shiftAhead(currentTime, daily)
    
    # for shifting towards type 0 EXPERIMENTAL
    def shiftAhead(self, currentGlobalTime, daily):
        localTime = currentGlobalTime % 288
        checkAheadRange = 288 - localTime
        checkBehindRange = localTime
        currentBest = None
        self.moveAhead = None

        if(self.getTimeInterval(daily, currentGlobalTime) == 0):
            return None

        for i in range(checkAheadRange):
            aheadTime = localTime + i
            currentType = self.getTimeInterval(daily, aheadTime)
            
            if(currentType == 0):
                # return 0
                currentBest = i
                break
        
        for i in range(checkBehindRange):
            behindTime = localTime - i
            currentType = self.getTimeInterval(daily, behindTime)

            if(currentType == 0):
                if(currentBest == None):
                    # return 1
                    # currentBest = i
                    return 0
                    # break
                elif(i < currentBest):
                    # currentBest = i
                    return 0
                else:
                    return 1
                    # break
                    # return 1
        
        return None








# ---------ERROR CALCULATION---------
    def isTaken(self, tfType):
        if(tfType == 0):
            return True
        elif(tfType == 1):
            # if random.uniform(0, 1)*10 <= 8:
            if random.randint(0, 100) < 80:
                return True
        elif(tfType == 2):
            # if random.uniform(0, 1)*10 <= 2:
            if random.randint(0, 100) < 20:
                return True
        return False

    def calculateErrorRate(self):
        taken = []
        # print(self.intervalsTaken)
        for i in self.intervalsTaken:
            taken.append(self.isTaken(i))
        notTaken = 0
        # print(taken)
        for i in taken:
            if i == False:
                notTaken += 1
        
        return notTaken / len(taken)
        
    
    
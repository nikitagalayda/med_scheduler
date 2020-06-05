from medicine import Medicine
import math

# STARTING AT 08:00
# daily = [
#     (0, 0),
#     (6, 2),
#     (12, 1),
#     (48, 0),
#     (60, 1),
#     (120, 2),
#     (126, 1),
#     (132, 0),
#     (144, 2),
#     (150, 0),
#     (192, 2),
#     (288, 0),
# ]

# STARTING AT 12:00
daily = [
    (0,0),      # 12-13
    (12, 1),    # 13-18
    (72, 2),    # etc
    (78, 1),    
    (84, 0),
    (96, 2),
    (102, 0),
    (144, 2),
    (240, 0),
    (246, 2),
    (252, 1),
    (288, 0),
]

num_intervals = 168*60/5

def getTimeInterval(time):
    for i in range(len(daily)):
        time = time % 288
        if(time < daily[i][0]):
            return daily[i-1][1]

def stringifyList(my_list):
    my_str = ""
    for i in my_list:
        if i != 0:
            my_str = my_str + " " + str(i)
        else:
            my_str = str(i)
    
    return my_str

def outputToFile(output):
    f = open("schedule.txt", "w")
    f.write(output)
    f.close()

med_1 = Medicine(1, 86, 106, 0, [], -1)
med_2 = Medicine(2, 64, 80, 0, [], -1)
med_3 = Medicine(3, 129, 159, 0, [], -1)
med_4 = Medicine(4, 259, 317, 0, [], -1)

medicines = [med_1, med_2, med_3, med_4]

for med in medicines:
        med.takeMedicine()
        med.intervalsTaken.append(getTimeInterval(1))

output = "0800 4 1 2 3 4\n"

# test_range = 100
# total_performance = [0, 0, 0, 0]

# for tests in range(test_range):
for i in range(int(num_intervals)):
    # Main loop where each iteration is a 5 minute inverval
    takenMedicines = []
    for med in medicines:
        med.updateTime()
        conditional = med.minTimePassed()

        if((med.moveAhead != None) and (med.moveAhead == 1)):
            conditional = med.atMaxTime()
        if(conditional):
            med.checkAhead(i, daily)
            if(med.preferredTake < 0):
                med.takeMedicine()
                takenMedicines.append(med.name)
                med.intervalsTaken.append(getTimeInterval(i))
            else:
                if(i == med.preferredTake):
                    med.takeMedicine()
                    takenMedicines.append(med.name)
                    med.intervalsTaken.append(getTimeInterval(i))

    if(len(takenMedicines) != 0):
        hours = str(math.floor((i * 5) / 60) + 8)
        if(len(hours) == 1):
            hours = "0" + hours
        mins = str((i * 5) % 60)
        if(len(mins) == 1):
            mins = "0" + mins

        curr_output = hours + mins + " " + str(len(takenMedicines)) + stringifyList(takenMedicines)
        
        output += (curr_output + "\n")

outputToFile(output)
        
    # idx = 0
    # for med in medicines:
    #     total_performance[idx] += med.calculateErrorRate()
    #     idx += 1


# result = list(map(lambda x : (x / test_range), total_performance))

# Print average result of test_range runs
# Format: [med_1, med_2, med_3, med_4] in percentages
# print(result)

idx = 0
for med in medicines:
    print("Medicine {}: {}".format(idx+1, medicines[idx].calculateErrorRate()))
    # print("Shifts AHEAD: {}".format(medicines[idx].shifts['1']))
    # print("Shifts BEHIND: {}".format(medicines[idx].shifts['0']))
    # print("Shift times: {}".format(medicines[idx].shiftTimes))
    idx += 1
    



# print(med_1.intervalsTaken)
# print(len(med_1.intervalsTaken))
# idx = 0
# performances = [0, 0, 0, 0]
# for med in medicines:
#     print("Medicine {}: ".format(idx+1, medicines[idx].calculateErrorRate()))
#     print("Shifts AHEAD: {}".format(medicines[idx].shifts['1']))
#     print("Shifts BEHIND: {}".format(medicines[idx].shifts['0']))
#     print("Shift times: {}".format(medicines[idx].shiftTimes))
#     idx += 1
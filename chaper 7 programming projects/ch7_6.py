# harrison frahn
# period 2
# chapter 7.6
# expected input: the start time and end time, separated by a comma.
# assuming that 12:00PM = noon and 12:AM = midnight
NOTE TO SELF: ADD EOFERROR HANLDING TO OTHER PROJECTS! 
also fix 23:23 to 23:23 problem (something to do with float rounding??)
from math import floor
def calcCost(startTime, endTime):
    cost = 0
    currentTime = startTime
    if endTime - startTime <= 0:
        endTime += 24
    for i in range(floor(endTime-startTime)):
        if currentTime >= 24:
            currentTime = 0
        cost += 100
        if(currentTime >= 19):
            cost += 50
        currentTime += 1
    if endTime >= 24:
        endTime -= 24
    if (endTime-currentTime > 0 and startTime != endTime) or (currentTime == startTime and startTime!= endTime):
        if currentTime<19:  
            cost += 100/60*(endTime-currentTime)*60
        elif currentTime>=19:
            cost += 150/60*(endTime-currentTime)*60
    return cost
def to_24(time):
    am_or_pm = time[len(time)-2:]
    if len(time) < 7 and (am_or_pm.lower()=='am' or am_or_pm.lower()=='pm'):
        first2 = str(int(time[0]))
    else:
        first2 = str(int(time[:2]))
    if len(time) <  7 and (am_or_pm.lower()=='am' or am_or_pm.lower()=='pm'):
        last2 = str(int(float(str((100/60)*int(time[2:4])))))
    else:
        last2 = str(int(float(str((100/60)*int(time[3:5])))))
    if am_or_pm.lower() != 'am' and am_or_pm.lower() != 'pm':
        print(last2)
        return float(first2 + "." + last2)
    else:
        if am_or_pm.lower() == 'pm' and first2 != "12" and len(time) > 7:
            first2 = str(12+int(time[:2]))
        else:
            first2 = str(12+int(time[0]))
        if am_or_pm.lower() == 'am' and first2 == '12':
            first2 = '00'
        return float(first2 + '.' + last2)
def main():
    print("This program calculates the cost of Mr. Friedland's tutoring services.")
    try:
        startTime = input("Please enter the starting time of the tutoring period. The time can either be 24-hour or followed by am/pm.\n")
        endTime = input("Please enter the ending time of the tutoring period: ")
        st1 = to_24(startTime)
        et1 = to_24(endTime)
        cost = calcCost(st1,et1)
        print("Your cost: ${0:0.2f}.".format(cost))
    except ValueError:
        print("It looks like you entered your times wrong! Remember, you can either enter them like this: 1:00am, 10:00pm; or like this: 01:00, 22:00.")
    except EOFError:
        print("\n")
    except KeyboardInterrupt:
        print("\n")
    except:
        print("Something went wrong!")
main()
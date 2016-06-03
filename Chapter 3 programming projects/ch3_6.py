# harrison Frahn
# period 2
# chapter 3.6
# expected input: an integer
import math
def main():
    print("This program calculates the value of pi/4 using an infinite series")
    x = eval(input("Enter the number of times to iterate the sequence: "))
    while(x%1!=0):
        x = eval(input("You didn't enter an integer! Please enter the number of times to iterate the sequence: "))
    initial = 1
    plusOrMinus = 0
    divisor = 3
    for i in range(0,x-1,1):
        if(plusOrMinus%2==0):
            initial -= 1/divisor
            plusOrMinus += 1
            divisor += 2
        elif(plusOrMinus%2==1):
            initial += 1/divisor
            plusOrMinus += 1
            divisor += 2
    print("Approximated value =", initial)
    print("Possible error =", math.pi/4-initial)
main()

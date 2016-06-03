# chaos.py
# example of chaotic behavior
def main():
    print("This program illustrates a chaotic function")
    y = eval(input("How many values should I print?"))
    x = eval(input("Enter a number between 0 & 1:"))
    z = eval(input("Enter another number: "))
    print("Value 1:    Value 2:")
    for i in range(y):
        x = 3.9 * x  - 3.9 * x * x
        z = 3.9 * z  - 3.9 * z * z
        print("{0:.6f}".format(x), end = '    ')
        print("{0:.6f}".format(z))
main()

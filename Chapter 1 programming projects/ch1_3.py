# chaos.py
# example of chaotic behavior
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 & 1:"))
    for i in range(20):
        x = 2.0 * x * (1-x)
        print(x)
main()

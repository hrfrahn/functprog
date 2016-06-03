# harrison frahn
# period 2
# chapter 5.3
# expected input: a string
def main():
    print("This is an acronym creator.")
    string = input("Enter a sentence to make an acronym of: ")
    x = string.split()
    for i in range(len(x)):
        if x[i] == 'of' or x[i] == 'Of' or x[i] == 'the' or x[i] == 'The' or x[i] == 'and' or x[i] == 'And':
            pass
        else:
            y = x[i].upper()
            print(y[0],end="")
    print("")
main()

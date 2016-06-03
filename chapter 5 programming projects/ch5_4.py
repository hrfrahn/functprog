# harrison frahn
# period 2
# chapter 5.3
# expected input: a file name
def main():
    print("This program counts words,characters, and spaces.")
    fileName = input("Enter the file to be read:")
    file = open(fileName,'r')
    data = file.read()
    chars = len(data)
    print("Characters:",str(chars))
    spaces = data.split()
    print('Spaces:',str(len(spaces)))
    lines = data.split('\n')
    print("Lines:",str(len(lines)))
main()
    

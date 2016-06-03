# harrison frahn
# period 2
# chapter 6.1
# expected input: a string
def right_justify(word):
    for i in range(70-len(word)):
        print(" ", end = "")
    print(word)
def main():
    word = input("Enter a word to be right-justified: ")
    right_justify(word)
main()

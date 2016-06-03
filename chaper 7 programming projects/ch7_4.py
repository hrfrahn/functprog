# harrison frahn
# period 2
# chapter 7.4
# expected input: a number
def grade(number):
    number = round(number)
    if number number >= 88:
        return 'A'
    elif number <= 87 and number >= 77:
        return 'B'
    elif number <= 76 and number >= 66:
        return 'C'
    elif number <= 65 and number >= 55:
        return 'D'
    elif number <= 54:
        return 'F'
def main():
    try:
        score = eval(input("Enter your score out of 100: "))
        x = grade(score)
        print("Your grade is:",x)
    except NameError:
        print("You entered letters, not a number!")
    except SyntaxError:
        print("Either you didn't enter any number, or you entered the number wrong!") 
    except TypeError:
        print("You entered more than 1 number!")
    except KeyboardInterrupt:
        print("\n")
    except:
        print("Something went wrong!!")
if __name__ == '__main__':
    main()
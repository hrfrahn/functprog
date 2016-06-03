# harrison frahn
# period 2
# chapter 8.1
# expected input: the number of times to iterate the sequence
#                 and then whether or not to do it again.
def getVal(times):
    first = 1
    if times == 0:
        return 1
    current = 2
    for i in range(times-2):
        next1 = first*current
        first = current
        current = next1
    return current
def main():
    print("This program calculates the sequence where the next term is the product of the previous 2.")
    again = True
    try:
        while again == True:
            times = eval(input("Enter the number of times to iterate the sequence: "))
            print(getVal(times))
            a = input("Calculate the sequence again? Enter Y or N: ")
            if a[0].lower() != 'y':
                again = False
            if a[0].lower() != 'y' and a[0].lower() != 'n':
                raise RuntimeError
    except NameError:
        print("You entered letter(s), not a number!")
    except SyntaxError:
        print("You entered the number wrong!")
    except TypeError:
        print("You entered more than 1 number!")
    except RuntimeError:
        print("You didn't enter Y or N!")
    except KeyboardInterrupt or EOFError:
        print('\n')
    except:
        print("Something went wrong!")
main()


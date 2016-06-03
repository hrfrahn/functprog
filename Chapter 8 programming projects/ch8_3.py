# harrison frahn
# period 2
# chapter 8.3
# expected input: a prime and an integer
def isprime(num):
    if num%1!=0:
        return False
    num = abs(num)
    # 1 and 0 aren't prime
    if num < 2:
        return False
    # 2 is the only even prime
    if num == 2: 
        return True
    # after we're sure n isn't 2, return false if n is even
    if num%2==0: 
        return False
    # check all the rest of the nums up to sqrt(n)
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True
def main():
    again = True
    try:
        while again:
            print('This program demonstrates Fermat\'s little theroem.')
            p = eval(input("Enter a prime: "))
            a = eval(input("enter an integer: "))
            if isprime(p) and a%1==0:
                mult = a**p
                fact = (mult - a)//p
                print('a =',a,'\np =',p)
                print(a,'^',p,'=',int(mult))
                print('(',int(mult),'-',a,') /',p,'=',int(fact))
                print(mult-a,'is an integer multiple of',p,'so the theroem works! YAY!')
            elif isprime(p)==False and a%1!=0:
                raise RuntimeError("You didn't enter a prime number or an integer!")
            elif isprime(p)==False:
                raise RuntimeError("You didn't enter a prime number!")
            elif a%1!=0:
                raise RuntimeError("You didn't enter an integer!")
            a = input('Demonstrate the theorem again, with different values?(y/n)')
            if a[0].lower() != 'y':
                again = False
            if a[0].lower() != 'y' and a[0].lower() != 'n':
                raise RuntimeError("You didn't enter y or n!")
    except RuntimeError as err:
        print(err.args)
    except NameError:
        print("You entered letter(s), not a number!")
    except TypeError:
        print("You entered more than 1 number!")
    except SyntaxError:
        print("You entered the number wrong!")
    except EOFError or KeyboardInterrupt:
        print('\n')
    except:
        print("Something went wrong!")
main()

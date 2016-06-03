# harrison frahn
# period 2
# chapeter 5.5
# expected input: loan amount, loan term, and monthly interest rate
def main():
    print("This program calculates the interest of an amortization loan.")
    p = eval(input("Enter the loan amount: "))
    balance = float(p)
    i = eval(input("Enter the yearly interest rate: "))
    i /= 1200
    n = eval(input("Enter the loan term (in years): "))
    n *= 12
    monthlyPayment = (i * p *(1+i)**n)/((1+i)**n-1)
    print(monthlyPayment)
    totalPayment = monthlyPayment * 360
    totalInterest = totalPayment - p
    print("Payment#:    Amount:     Principal:     Interest:     Balance:")
    for x in range(1,n+1,1):
        monthInterest = balance * i
        monthPayment = monthlyPayment - monthInterest
        balance -= monthPayment
        if(x<n):
            print("{0:8}     {1:0.6}     {2:0.2f}         {3:0.2f}       {4:0.2f}".format(x,monthlyPayment,monthPayment,monthInterest,balance))
        elif(x==n):
            print("{0:8}     {1:0.6}     {2:0.2f}         {3:0.2f}        0".format(x,monthlyPayment,monthPayment,monthInterest))
main()

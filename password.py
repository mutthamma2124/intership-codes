password=1234
balance=1000
def withdraw():
    print("enter amount to withdraw:")
    if(balance>1000):
        print("the amount is higher than the balance")
    else:
        print("the amount is sufficient")
def default():
    print("amount is not there")
def amount():
    some=int(input("enter amount"))
    data={1:withdraw}
    result=data.get(some,default)
    result()

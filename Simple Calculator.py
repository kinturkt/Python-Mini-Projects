def sum(a,b):
    print("The answer is:",a+b)
def diff(a,b):
    print("The answer is:",a-b)
def mul(a,b):
    print("The answer is:",a*b)
def div(a,b):
    print("The answer is:",float(a/b))

a,b=map(int,input("Enter numbers:").split())
c=input("Enter a operator:")
if c=="+":
    sum(a,b)
elif c=="-":
    diff(a,b)
elif c=="*":
    mul(a,b)
elif c=="/":
    div(a,b)
else:
    print("Invalid operator")
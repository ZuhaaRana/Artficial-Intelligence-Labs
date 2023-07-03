
def AND(x, y):
    return x and y

def OR(x,y):
    return x or y

def NOT(x):
    return not x

def IF(x,y):
    return not(x=="T" and y=="F")

def IF_AND_ONLY_IF(x,y):
    return x and y

print("LOGICAL OPERATORS")
P,Q=input("Enter the value of P and Q :").split()
print("AND Operator", AND(P,Q))
print("OR Operator", OR(P,Q))
print("NOT Operator", NOT(P))
print("IF Operator",IF(P,Q))
print("IF and Only IF",IF_AND_ONLY_IF(P,Q))

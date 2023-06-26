
# Constraint Satisfaction Problems

# 3.3
# Find all (a,b,c) where a ∈ {3,7,9,3,6} and b ∈ {7,8,9,10}  where ‘a’ should # be a+1
# equal to b and a not equal to c.



from constraint import *
p = Problem()
p.addVariable("a",[1,2,3])
p.addVariable("b",[1,2,3])

print("Solutions without constraints : ",p.getSolutions())
p.addConstraint(lambda a,b: a+1 == b,["a","b"])

print("Solutions with constraints : ",p.getSolutions())



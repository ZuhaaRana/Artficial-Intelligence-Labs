
# Constraint Satisfaction Problems

# 3.2
# Find all (a,b) where a ∈ {1,2,3} and b ∈ {1,2,3}  where ‘a’ should be
# +1 equal to b .

from constraint import *
p = Problem()
p.addVariable("a",[1,2,3])
p.addVariable("b",[1,2,3])

print("Solutions without constraints : ",p.getSolutions())
p.addConstraint(lambda a,b: a+1 == b,["a","b"])

print("Solutions with constraints : ",p.getSolutions())



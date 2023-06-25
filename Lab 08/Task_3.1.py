
#Constraint Satisfaction Problems

# 3.1
# Find all (a,b) where a ∈ {1,2,3} and b ∈ {4,5,3} where ‘a’ should b
# a*2 equal to b .

from constraint import *
p = Problem()
p.addVariable("a",[1,2,3])
p.addVariable("b",[4,5,6])

print("Solutions without constraints : ",p.getSolutions())
p.addConstraint(lambda a,b: a*2 == b,["a","b"])

print("Solutions with constraints : ",p.getSolutions())

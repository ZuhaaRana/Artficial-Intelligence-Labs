
# Constraint Satisfaction Problems

# 3.4
# All the combinations of R, G, B

from constraint import *

p = Problem()
p.addVariable("A",['R','B','G'])
p.addVariable("B",['R','B','G'])
p.addVariable("C",['R','B','G'])
p.addVariable("D",['R','B','G'])

p.addConstraint(lambda A,B: A != B,["A","B"])
p.addConstraint(lambda A,C: A != C,["A","C"])
p.addConstraint(lambda A,D: A != D,["A","D"])
p.addConstraint(lambda B,D: B != D,["B","D"])
p.addConstraint(lambda C,D: C != D,["C","D"])

print("Solutions : ", p.getSolutions())





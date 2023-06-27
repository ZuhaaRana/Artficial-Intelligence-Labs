
# Constraint Satisfaction Problems

# 3.6
# Define a problem with no solution.

from constraint import *
p = Problem()

p.addVariable("A",['R','B','G'])
p.addVariable("B",['R','B','G'])
p.addVariable("C",['R','B','G'])
p.addVariable("D",['R','B','G'])
p.addVariable("E",['R','B','G'])
p.addVariable("F",['R','B','G'])
p.addVariable("G",['R','B','G'])
p.addVariable("H",['R','B','G'])

p.addConstraint(lambda A,B: A != B,["A","B"])
p.addConstraint(lambda A,C: A != C,["A","C"])
p.addConstraint(lambda B,D: B != D,["B","D"])
p.addConstraint(lambda C,D: C != D,["C","D"])
p.addConstraint(lambda C,B: C != B,["C","B"])
p.addConstraint(lambda C,E: C != E,["C","E"])
p.addConstraint(lambda E,F: F != F,["E","F"])
p.addConstraint(lambda E,C: E != C,["E","C"])
p.addConstraint(lambda F,D: F != D,["F","D"])
p.addConstraint(lambda F,G: F != G,["F","G"])

print("Total Solutions : ",len(p.getSolutions()))

print("Solutions : ",p.getSolutions())

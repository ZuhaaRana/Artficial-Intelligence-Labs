# CSP Problem

from constraint import *

p = Problem()

# ADDING ALL THE REQUIRED VARIABLES

p.addVariable("Up", ['3:30 pm (SATURDAY)', '8:30 pm (SATURDAY)',
                     '3:30 pm (SUNDAY)', '8:30 pm (SUNDAY)'])

p.addVariable("Caption_America", ['3:30 pm (SATURDAY)', '8:30 pm (SATURDAY)',
                                  '3:30 pm (SUNDAY)', '8:30 pm (SUNDAY)'])

p.addVariable("When_a_Stranger", ['3:30 pm (SATURDAY)', '8:30 pm (SATURDAY)',
                                  '3:30 pm (SUNDAY)', '8:30 pm (SUNDAY)'])

p.addVariable("Sully", ['3:30 pm (SATURDAY)', '8:30 pm (SATURDAY)',
                        '3:30 pm (SUNDAY)', '8:30 pm (SUNDAY)'])

# ADDING ALL THE REQUIRED CONSTRAINTS

p.addConstraint(lambda Up, Caption_America: Up != Caption_America, ["Up", "Caption_America"])

p.addConstraint(lambda Up, When_a_Stranger: Up != When_a_Stranger, ["Up", "When_a_Stranger"])

p.addConstraint(lambda Up, Sully: Up != Sully, ["Up", "Sully"])

p.addConstraint(lambda Caption_America,
                       When_a_Stranger: Caption_America != When_a_Stranger,
                ["Caption_America", "When_a_Stranger"])

p.addConstraint(lambda Caption_America,
                       Sully: Caption_America != Sully,
                ["Caption_America", "Sully"])

p.addConstraint(lambda When_a_Stranger,
                       Sully: When_a_Stranger != Sully,
                ["When_a_Stranger", "Sully"])

# DISPLAY OUTPUT
print("Solutions : ", p.getSolutions())

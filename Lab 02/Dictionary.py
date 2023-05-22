
# Check if a given dict already exists in a dictionary.
# For a given list, you can also check whether our child dictionary
#exists in the main dictionary or not. Here we have two sub
#-dictionaries “Boys” and “Girls”, now we want to check whether our
#dictionary Boys exist in our main “Dict” or not. For that, we use the
#for loop method with else if method.

# Example 1:
# Dict = {'Hannan': 18,'Waleed':12,'Arfa':22,'Ali':25}
# Boys = {'Hannan': 18,'Waleed':12,'Ali':25}
# Girls = {'Arfa':22}


Dict={'Hannan': 18,'Waleed':12,'Arfa':22,'Ali':25}
Boys={'Hannan':18, 'Waleed':12,'Ali':25}

A=0
for D in Dict:
    for B_Dictionary in Boys:
        if(D==B_Dictionary):
            A+=1
if(A==len(Boys)):
    print("Boys Dictionary exists in the main dictionary")
else:
    print("Boys Dictionary doesn't exist in the main dictionary")

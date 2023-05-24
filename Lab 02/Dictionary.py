
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
Girls = {'Ayesha':22}

B=0
for D in Dict:
    for B_Dictionary in Boys:
        if(D==B_Dictionary):
            B+=1
            
G=0
for D in Dict:
    for G_Dictionary in Girls:
        if(D==G_Dictionary):
            G+=1
            
if(B==len(Boys)):
    print("Boys Dictionary exists in the main dictionary")
else:
    print("Boys Dictionary doesn't exist in the main dictionary")
    
if(G==len(Girls)):
    print("Girls Dictionary exists in the main dictionary")
else:
    print("Girls Dictionary doesn't exist in the main dictionary")
    

# There is cleaning robot named ”SAXON”, It is going to clean room and
# pool. It will clean the
# room by calculating its area and pool by calculating its volume.
# Take the values from user for specified inputs
# Create a class Saxon and two functions Room and Pool. In each
#function it will ask the
# corresponding input values from user to calculate its area and
#volume. 
#And then display on the screen that I am going to clean Room with " "
#area and Pool with “ ” volume.

class SAXON:
    def Room(self):
        length = int(input("Enter length for room : "))
        width = int(input("Enter width for room : "))
        area = length*width
        print("Area of room is : ",area)
        print("I am going to clean Room with",area, "area")

    def Pool(self):
        print()
        length = int(input("Enter length for pool : "))
        width = int(input("Enter width for pool : "))
        depth = int(input("Enter depth for pool : "))
        vol = length * width * depth
        print("Volume of pool is : ",vol)
        print("I am going to clean Pool with",vol,"volume.")

S = SAXON()
S.Room()
S.Pool()


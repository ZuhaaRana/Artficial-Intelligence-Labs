#Min Max Algorithm

import math
def MINMAX(current_depth,node,max_turn,score,total_depth):
    if(current_depth==total_depth):
        return score[node]
    if(max_turn):
        return max(MINMAX(current_depth+1,node*2,False,score,total_depth),
                   MINMAX(current_depth+1,node*2+1,False,score,total_depth))
    else:
        return min(MINMAX(current_depth+1,node*2,True,score,total_depth),
                   MINMAX(current_depth+1,node*2+1,True,score,total_depth))

score =[]
x = int(input("Enter total leaf nodes : "))
for i in range(x):
    y = int(input("Enter the value of leaf node : "))
    score.append(y)

total_depth = math.log(len(score),2)
current_depth = int(input("Enter current depth : "))
node = int(input("Enter node value : "))
max_turn=True
print("The answer according to the minmax algorithm is : ",end=" ")
answer=(MINMAX(current_depth,node,max_turn,score,total_depth))
print(answer)

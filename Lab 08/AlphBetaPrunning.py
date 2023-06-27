# Alpha Beta Prunning

maximun_value, minimum_value = 1000,  -1000

def ALPHA_BETA_PRUNNING(depth, nodeIndex, max_Player, values, alpha_value, beta_value):
    if depth == 4:
        return values[nodeIndex]

    if max_Player:
        for i in range(0, 2):
            value = ALPHA_BETA_PRUNNING(depth + 1, nodeIndex * 2 + i,False, values, alpha_value, beta_value)
            optimal_value = max(minimum_value, value)
            alpha_value = max(alpha_value, minimum_value)
            if beta_value <= alpha_value:
                break
        return optimal_value
    else:
        for i in range(0, 2):
            value = ALPHA_BETA_PRUNNING(depth + 1, nodeIndex * 2 + i, True, values, alpha_value, beta_value)
            optimal_value = min(maximun_value, value)
            beta_value = min(beta_value, maximun_value)
            if beta_value <= alpha_value:
                break
        return optimal_value

if __name__ == "__main__":
    assigned_values = [4,3,6,2,2,1,9,5,3,1,5,4,7,5] 

    print("The value acording to alpha beta prunning is ", ALPHA_BETA_PRUNNING(0, 0, True, assigned_values, minimum_value, maximun_value))

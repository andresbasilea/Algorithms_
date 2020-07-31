import numpy as np





def edit_distance(s, t):


    matrix = [[0 for x in range(len(s)+1)] for x in range(len(t)+1)]


    for i in range(len(s)+1):
        matrix[0][i] = i
    for j in range(len(t)+1):
        matrix[j][0] = j
    #print(np.matrix(matrix), "\n")


    for j in range(1,len(t)+1):
        #matrix[j][0] = 55
        for i in range(1,len(s)+1):
            #matrix[0][i] = 66
            ins = matrix[j-1][i] + 1
            dele = matrix[j][i-1] + 1
            match = matrix[j-1][i-1]
            mismatch = matrix[j-1][i-1] + 1

            if s[i-1] == t[j-1]:
                matrix[j][i] = min(ins,dele,match)
            else:
                matrix[j][i] = min(ins, dele, mismatch)

    #print(np.matrix(matrix))
    return matrix[len(t)][len(s)]




if __name__ == "__main__":
    print(edit_distance(input(), input()))

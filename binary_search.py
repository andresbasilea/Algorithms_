# Uses python3
import sys
import math

def binary_search(a, x, left, right):
    if right >= left:
        medio = (left + right)//2
    # left, right = 0, len(a)

        if a[medio] == x:
            return medio
        elif a[medio]<x:
            return binary_search(a,x,medio+1,right)
        else:
            return binary_search(a,x,left,medio-1)

    else:
        return -1

# def linear_search(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        #print(x)
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)-1), end = ' ')

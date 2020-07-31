# Uses python3
import sys
import random

def partition3(a, l, r):
    i = l
    maq = r
    meq = l
    pivote = a[l]

    while i<= maq:
        if a[i] < pivote:
            a[meq],a[i]=a[i],a[meq]
            meq += 1
            i += 1
        elif a[i] > pivote:
            a[i],a[maq] = a[maq],a[i]
            maq -= 1
        else:
            i+=1

    return meq, maq

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    meq, maq = partition3(a,l,r)
    randomized_quick_sort(a, l, meq - 1);
    randomized_quick_sort(a, maq + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

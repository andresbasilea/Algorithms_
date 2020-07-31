# Uses python3
import sys


infinito = 10000


def get_change(money):

    coins = [1,3,4]


    # minNumCoins = [0 for j in range(money)]
    # print(minNumCoins)
    # for m in range(1,money):
    #     minNumCoins[m] = infinito
    #     print(minNumCoins)
    #     for i in range(1,len(coins)):
    #         if m >= coins[i]:
    #             numCoins = minNumCoins[m-i] + 1
    #             if numCoins < minNumCoins[m]:
    #                 minNumCoins[m] = numCoins
    # return minNumCoins[money-1]



    # minNumMonedas = [infinito for x in range(money+1)]
    # minNumMonedas[0] = 0
    # print(minNumMonedas)
    #
    # for i in range(1,money+1):
    #     print(i)
    #     for j in range(len(coins)):
    #         print(j)
    #         if i >= coins[j]:
    #             numeroMonedas = minNumMonedas[i-(j+1)] + 1
    #             if numeroMonedas < minNumMonedas[i]:
    #                 minNumMonedas[i] = numeroMonedas
    # print(minNumMonedas)
    # return minNumMonedas[money]

    minNumMonedas = [infinito for x in range(money+1)]
    minNumMonedas[0] = 0

    for coin in coins:
        for j in range(coin, money+1):
            minNumMonedas[j] = min(minNumMonedas[j],minNumMonedas[j-coin]+1)

    if minNumMonedas[money] != infinito:
        return minNumMonedas[money]
    else:
        return -1



    #return money // 4

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))

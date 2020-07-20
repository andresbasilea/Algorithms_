# Uses python3
import sys
import math
from collections import Counter


# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b


def lcm(a,b):
	return int(a*b/gcd(a,b))


def gcd(a,b):
	if b == 0:
		return a
	a2 = a%b
	return gcd(b,a2)

	# lcm = []
	# aparecieron = []
	# lista = primeFactors(a)
	# lista2 = primeFactors(b)
	# print(lista, lista2)





	# for i in lista:
	# 	lcm.append(i)
	# for j in lista2:
	# 	lcm.append(j)


	# print(lcm)

	# frecuencias = {}
	# for l in lista:
	# 	if l in frecuencias:
	# 		frecuencias[l] += 1
	# 	else:
	# 		frecuencias[l] = 1
	# print(frecuencias)

	# frecuencias2 = {}
	# for k in lista2:
	# 	if k in frecuencias2:
	# 		frecuencias2[k] += 1
	# 	else:
	# 		frecuencias2[k] = 1
	# print(frecuencias2)

	# for key in frecuencias.keys():
	# 	if key in frecuencias2.keys():
	# 		if frecuencias[key] > frecuencias2[key]:
	# 			lcm.append(key * frecuencias[key]) 

	# print(lcm)
	# a1 = Counter(lista)
	# a2 = Counter(lista2)


	# compartidos = {k: a1[k] for k in a1 if k in a2 and a1[k] == a2[k]}
	# print(compartidos)


	# print(a1)
	# for k,v in a1.items():
	# 	print('elemento {} aparece {} veces'.format(k,v))



	# resultado = 1
	# for x in lcm:
	# 	resultado = resultado * x

	# return resultado


# def primeFactors(n): 

# 	arr = []

# 	while n % 2 == 0: 
# 		arr.append(2)
# 		n = n / 2
		  
# 	for i in range(3,int(math.sqrt(n))+1,2): 
# 		while n % i== 0: 
# 			arr.append(int(i))
# 			n = n / i 
			  
# 	if n > 2: 
# 		arr.append(int(n)) 

# 	return arr


if __name__ == '__main__':
	input = sys.stdin.read()
	a, b = map(int, input.split())
	print(lcm(a, b))


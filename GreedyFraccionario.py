import sys

class Objeto:
	def __init__(self, peso, valor):
		self.peso = peso
		self.valor = valor
		self.ratio = self.valor/self.peso

def impresora(stack,n):
	for k in range(n):
		print("Peso -> ", stack[k].peso, " valor -> ", stack[k].valor, " ratio -> ", stack[k].ratio)

def get_optimal_value(n,capacidad, weights, values):
	value = 0
	n = n
	# ratio = []
	stack = []
	peso = 0
	capacidad = capacidad


	for j in range(n):
		stack.append(Objeto(weights[j],values[j]))

	#impresora(stack,n)
	# print(stack)

	stack.sort(key=lambda x:x.ratio, reverse = True)

	#print("\n", "Ordenados!!")
	#impresora(stack,n)
	#print("\n")

	# for i in range(n):
	# 	ratio.append(int(stack[i].valor/stack[i].peso))

	#print("arreglo de elementos ", ratio)


	while (capacidad > 0) and (len(stack) != 0):
		if(stack[0].peso <= capacidad):
			#print(stack[0].ratio)
			capacidad -= stack[0].peso
			#print(capacidad)
			#peso += stack[0].peso
			value += stack[0].valor
			stack.pop(0)
			#impresora(stack,n-1)
		else:
			#print(stack[0].peso)
			aRestar = stack[0].peso-capacidad
			#print(aRestar)
			stack[0].peso -= aRestar
			#print(stack[0].peso)
			valorFraccional = stack[0].peso*stack[0].ratio
			value += valorFraccional
			capacidad = 0
			stack.pop(0)

	return value

if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	opt_value = get_optimal_value(n,capacity, weights, values)
	print(opt_value)

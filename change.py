# Uses python3
import sys

def get_change(m):
    
	valor_actual = m
	cantidad_monedas = 0

	while m/10 >= 1:
		m -= 10
		cantidad_monedas+=1
	while m/5 >= 1:
		m -= 5
		cantidad_monedas+=1
	while m!= 0:
		m-=1
		cantidad_monedas+=1

	return cantidad_monedas
	

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

#Modified fib is defined as followed: F(n) = (F(n-1))^2 + F(n-2)
#list = [f, s, n] where f and s are the first and second numbers in the sequence, 
#and we want to find the nth number
def modified_fib(list):
	first, second = list[0], list[1]
	sol = 0
	for i in range(3, list[2] + 1):
	    sol = second ** 2 + first
	    first, second = second, sol
	return sol

print(modified_fib([0,1,5]))
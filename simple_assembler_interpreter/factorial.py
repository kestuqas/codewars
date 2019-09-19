from tail_rezursion import tail_recursive, recurse
def factorial(n):
  if n == 0: return 1
  else: return factorial(n-1) * n 

@tail_recursive
def tail_factorial(n, accumulator=1):
  if n == 0: 
  	return accumulator
  recurse(n-1, accumulator = accumulator*n)
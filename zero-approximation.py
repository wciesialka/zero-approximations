from math import *

def prep_for_eval(func):
	func = func.replace("^","**")
	return func

def get_derivative(func):
	h = (2**-32)
	deriv = "((" + func.replace("x","(x+h)") +  ") - (" + func.replace("x","(x-h)") + "))/(2*h)"
	return deriv.replace("h",str(h))

def get_approximation(f_x,d_x,x):
	return x - ((eval(f_x))/(eval(d_x)))

def get_approximations(f_x,d_x,initial,maxi,precision=4):
	x = initial
	for n in range(1,maxi):
		x = get_approximation(f_x,d_x,x)
		print("x_" + str(n+1) + "=\t",round(x,precision))
	print("Given f(x) = ",f_x,", an initial approximation of ",initial,", and ",maxi," approximations, f(x) = 0 when x = ",round(x,precision))
	

def main():
	f_x = prep_for_eval(input("f(x) = \t"))
	x = eval(prep_for_eval(input("Initial Approximation for x = \t")))
	d_x = get_derivative(f_x)
	n = eval(prep_for_eval(input("n = \t")))
	precision = eval(input("Precision = \t"))
	get_approximations(f_x,d_x,x,n,precision)

if __name__ == "__main__":
	main()

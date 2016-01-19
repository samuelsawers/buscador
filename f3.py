
"""Imprimir los numeros pares desde el 40 hasta el 60, ambos inclusive"""
n=0
h=''
while n<=60:
	n+=1
	if n>=40 and n<=60 and n%2==0:
	    h += ' %i' % n
print h

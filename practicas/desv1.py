#foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
#print map(lambda x: x**2, foo)
"""
class Persona(object):
	edad = 18
	def __init__(self, nombre, nacionalidad):
		self.nombre = nombre
		self.nacionalidad = nacionalidad
	@classmethod
	def saludar(cls, nombre):
		print 'estoy saludando ' + nombre

#persona = Persona("Jose", "Mexico")
#print(persona.nombre)
Persona.saludar("Alberto")
"""
"""
def fib(n):
	a, b = 0, 1
	while b < n:
		print b,
		a, b = b, a + b

fib(2000)
"""
def f(p1, p2, *otros):
	for val in otros:
		print val

f(1, 2)
f(1, 2, 3)
f(1, 2, 3, 4)
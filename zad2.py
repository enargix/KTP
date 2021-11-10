# Bogomaz Ivan zadacha 2
def equation(a, b):
	if a == 0:
		if b == 0:
			return "bezlich"
		else:
			return "nema"
	n = (-b)/a
	float('{:.2f}'.format(n))
	return '%.2f' % n
print(equation(20, -100))
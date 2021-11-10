# Bogomaz Ivan zadacha 1
def digit(a):
	b = a
	c = 0
	while b != 0:
		if b // 10 == 0:
			c = b
			break
		else:
			b //= 10
	sum = a%10 + c
	return sum
print(digit(1923))
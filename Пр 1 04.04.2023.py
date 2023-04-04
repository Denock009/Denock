n = 10
i = 0
a1 = 0
a2 = 1
print(0)
while i < n:
	a1, a2 = a2, a1 + a2
	print(a2)
	i += 1
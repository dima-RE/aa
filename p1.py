import os
import numpy as np

ar = []
for i in range(17):
	ar.append([])
	if i == 0:
		for j in range(17):
			if j == 0:
				ar[i].append("╔")
			elif j == 16:
				ar[i].append("╗")
			elif j%2 == 0:
				ar[i].append("╦")
			else:
				ar[i].append("═══")
	elif i == 16:
		for j in range(17):
			if j == 0:
				ar[i].append("╚")
			elif j == 16:
				ar[i].append("╝")
			elif j%2 == 0:
				ar[i].append("╩")
			else:
				ar[i].append("═══")
	elif i%2 != 0:
		for j in range(0,17):
			if j%2 == 0:
				ar[i].append("║")
			else:
				ar[i].append(" 0 ")
	else:
		for j in range(0,17):
			if j == 0:
				ar[i].append("╠")
			elif j == 16:
				ar[i].append("╣")
			elif j%2 == 0:
				ar[i].append("╬")
			else:
				ar[i].append("═══")

print(ar,'\n')

for i in range(17):
	for j in range(17):
		print(ar[i][j], end="")
	print()
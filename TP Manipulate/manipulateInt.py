def multiply(num):
	for i in range(1, 11):
		print(num, "x", i, "=", num*i)

def suite(num):
	if (num < 1 or num > 106):
		return print("Error, n isn't between 1 and 106")
	res = [num]
	while (num != 1):
		if (num % 2 == 0):
			num //= 2
			res.append(num)
		else:
			num *= 3
			num += 1
			res.append(num)
	print("->".join(str(x) for x in res));

def missingNumber(*numbers):
	memory = []
	for num in numbers:
		if (num <= 0):
			return print("Error, please enter numbers better than 0")
		if (numbers.count(num) != 1):
			if (memory.count(num) != 1):
				print(num, "was enter more than 1 time :", numbers.count(num), "exactly !")
		if (memory.count(num) != 1):
			memory.append(num)
	memory.sort()
	if (memory[len(memory)-1] != len(memory)):
		print(memory[len(memory)-1] - len(memory), "numbers were forget")
	else:
		print("Congratulation you forgot nothing !!")
missingNumber(1,2,3,5,6,8,9,1, 10,11,23, 3, 6, 5)
# Reverse string
def inversion(string):
	tab = list(string)
	tab.reverse()
	return str().join(tab)

print(inversion('Hello World !'))

# Split string
def separate(string, separator):
	tab = string.split(separator)
	return tab

print(separate("Hello World !", " "))

# Count char
def counterChar(string, char):
	tab = list(string)
	count = 0
	for c in tab:
		if (c == char):
			count += 1
	text = ""
	if (count == 0):
		text = "The char " + char + " is not in the str " + string
	else :
		text = "The char " + char + " is in the str " + str(count) + " times"
	return text

print(counterChar("Hello World", "l"))
print(counterChar("His palm are sweaty,  knees weak, arms are heavy", "z"))
print(counterChar("One thing, I don't know why. It doesn't even matter how hard you try. Keep that in mind. I designed this rhyme. To explain in due time", "i"))

def MajMin(string, jump):
	if (jump == 0):
		return string.upper()
	if (len(string) < jump):
		return "The number is over than the length of the string"
	if (jump < 0):
		return "The number is less than 0"
	count = 0
	tab = list(string)
	tab[0] = tab[0].upper()
	for index in range(len(tab)):
		if (count == jump):
			tab[index] = tab[index].upper()
			count = 0
		count += 1
	return str().join(tab)

print(MajMin("Vive le vent d'hiver", 2))
print(MajMin("hello World", 1))
print(MajMin("Blue", 10))
print(MajMin("If you're not the most gifted, be the one who works the most ", 10))
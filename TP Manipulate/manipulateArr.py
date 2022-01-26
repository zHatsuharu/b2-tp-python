def flag(l, flag, value=None):
	if (flag == "count"):
		res = {}
		for val in l:
			if (val not in res):
				res[val] = l.count(val)
		return res
	if (flag == "len"):
		return len(l)
	if (flag == "append"):
		l.append(value)
		return l
	if (flag == "remove"):
		l.remove(value)
		return l


l = [
	22, 
	"bleu",
	True,
	"Hello",
	156,
	-2,
	"Str",
	"Hello",
	22,
	25,
	55
]

# print(flag(l, "count"))
# print(flag(l, "len"))
# print(flag(l, "append", "TEST"))
# print(flag(l, "remove", 22))

def maximum(l):
	return max(l)
def minimum(l):
	return min(l)
def moy(l):
	return round(sum(l)/len(l), 2)

notes1 = [12,15,18,20,8,10]
notes2=[0, 19, 11, 18, 4]

# print(maximum(notes1))
# print(minimum(notes1))
# print(moy(notes1))
# 
# print(maximum(notes2))
# print(minimum(notes2))
# print(moy(notes2))

def classe():
	return

Programmateam = {
	"Costa" : [18,15,17,20,8],
	"Kevin" : [20,19,16,20,19],
	"Valentin" : [18,19,17,18,15],
	"Benji" : [17, 14, 15, 17, 15],
	"Arthur" : [17, 15, 13, 19, 13]
}

print(classe(Programmateam, "best", 1))
print(classe(Programmateam, "worst", 1))
print(classe(Programmateam, "moy", 1))
print(classe(Programmateam, "moySomeone", "Kevin"))
print(classe(Programmateam, "moyTotal",1 ))
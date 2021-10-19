a = {}
k = 0
f = open('input.txt', 'r')
maxk = 0
maxname = None
gg = True
for j in range(2000000000):
	candidate = f.readline()
	if candidate == '':
		break
	elif candidate in a:
		a[candidate]+=1
	else:
		a[candidate] = 1
for i in a:
	if a[i]==max(a.values()) and (a[i]/sum(a.values()))>0.5:
		print(i)
		gg = False
		break
	elif a[i]==max(a.values()):
		print(i)
	elif a[i]>maxk:
		maxk = a[i]
		max_name = i
if maxk!=0 and gg:
	print(max_name)
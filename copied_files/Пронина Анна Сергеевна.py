import sys
f = sys.stdin
s = set()
d = {}
k = 0
for l in f:
    k += 1
    a = l[:len(l)-1]
    if l in s:
        d[a] = int(d[a]) + 1
    else:
        s.add(l)
        d[a] = 1
m1 = 0
m2 = 0
M1 = ""
M2 = ""
for i in dict.keys(d):
    if (int(d[i])>k//2):
        print(i)
        sys.exit()
    elif (int(d[i])>m1):
        M2 =M1
        m2=m1
        m1 =int(d[i])
        M1 = i
    elif (int(d[i])>m2):
        m2 = int(d[i])
        M2 = i
print(M1)
print(M2)
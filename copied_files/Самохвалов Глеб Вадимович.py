cnt = 0
d = {}
flag = True
fout = open('output.txt','w')
with open('input.txt', encoding="utf-8") as f:
    for name in map(str.strip, f):
        d[name] = d.get(name, 0) + 1
        cnt += 1

for k, v in d.items():
    if v > (cnt / 2):
        print(k,file=fout)
        flag = False
d = sorted(d.items(), key=lambda x: x[1], reverse=True)
if flag:
    print(d[0][0],file=fout)
    print(d[1][0],file=fout)

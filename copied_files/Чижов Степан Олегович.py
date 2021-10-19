d = {}
cnt = 0

with open('input.txt') as f:
    name = f.readline().strip()
    while name:
        d[name] = d.get(name, 0) + 1
        cnt += 1
        name = f.readline().strip()

d = sorted(d.items(), key=lambda x: (-x[1]))
if d[0][1]/cnt > 0.5:
    print(d[0][0])
else:
    print(d[0][0], d[1][0], sep='\n')
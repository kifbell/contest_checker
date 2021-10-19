dct = dict()
cnt = 0
with open("input.txt") as file:
    for line in file:
        line = line.split('\n')
        if (not len (line)): break
        cnt += 1
        dct[line[0]] = dct.get(line[0], 0) + 1   

v =(list(sorted(dct.items(), key=lambda item: item[1])))
if (v[-1::][0][1] * 2 > cnt):
    print(v[-1::][0][0])
else:
    print(v[-1::][0][0])
    print(v[-2::][0][0])
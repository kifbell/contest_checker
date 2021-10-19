def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

import sys
a = sys.stdin
sl = {}
for i in a:
    if i in sl.keys():
        sl[i] += 1
    else:
        sl[i] = 1
count = 0
zap = ''
for h in sl.keys():
    if sl[h] > sum(sl.values()) * 0.5:
        count += 1
        zap = h
m1 = 0
m2 = 0
ch1 = 0
ch2 = 0
if count == 1:
    print(zap)
else:
    for h in sl.keys():
        if sl[h] > ch1:
            m1 = h
            ch1 = sl[h]
    del sl[f'{get_key(sl, ch1)}']
    for s in sl.keys():
        if sl[s] > ch2:
            m2 = s
            ch2 = sl[s]
    print(m1, end='')
    print(m2, end='')
f = open('input.txt', 'r', encoding='utf-8')
res = {}
k = 0
for s in f:
    if not s in res:
        res.update({s: 0})
    res[s] += 1
    k += 1

ans = sorted(res, key=res.get, reverse=True)

if res[ans[0]] * 2 > k:
    print(ans[0])
else:
    print(ans[0])
    print(ans[1])
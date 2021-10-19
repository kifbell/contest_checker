f = open('input.txt', 'r', encoding='utf-8')

candidates = {}
votes = 0

for line in f:
    votes += 1
    candidates[line.strip()] = candidates.get(line.strip(), 0) + 1




winner = False
for can in candidates:

    if candidates[can] > votes / 2:

        print(can)
        winner = True
        break

if winner == False:
    x = {value: [] for key, value in candidates.items()}
    for i in candidates.items():
        x[i[1]].append(i[0])

    print(* x[sorted(x.keys())[-1]])
    print(* x[sorted(x.keys())[-2]])

import re

with open("input.txt", encoding = 'utf-8') as f:
    votes = f.readlines()

candidates = {}
found = False
votes_checked = []
last = False

for i in range(len(votes)):
    if votes[i] == "\n":
        pass
    else:
        votes_checked.append(votes[i])

for i in range(len(votes_checked)):
    votes_checked[i] = re.sub("\n", "", votes_checked[i])
    if not(votes_checked[i] in candidates):
        candidates[votes_checked[i]] = 1
        if candidates[votes_checked[i]] > 0.5 * len(votes_checked):
            print(votes_checked[i])
            found = True
            break
    else:
        candidates[votes_checked[i]] += 1
        if candidates[votes_checked[i]] > 0.5 * len(votes_checked):
            print(votes_checked[i])
            found = True
            break

if not(found):
    top = max(candidates, key=candidates.get)
    candidates[top] = 0
    print(top + '\n' + max(candidates, key=candidates.get))
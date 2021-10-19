with open('input.txt', 'r') as file:
    election = dict()
    allK = []
    num_votes = 0

    # сделал список кандидатов
    for line in file:
        if line == '':
            break
        allK.append(line.replace('\n', ''))
        num_votes += 1

# сделал неупорядоченный словарь
for i in allK:
    if i in election:
        election[i] += 1
    else:
        election[i] = 1

# сделал упорядоченный словарь
sorted_values = sorted(election.values())
sorted_election = {}

for i in sorted_values:
    for k in election.keys():
        if election[k] == i:
            sorted_election[k] = election[k]
            break

# вывод
max_vote = max(election.values())
p = 0
if max_vote * 2 > num_votes:
    for k, votes in sorted_election.items():
        if votes == max_vote:
            ourPresident = k
            print(ourPresident)
else:
    for k, votes in sorted_election.items():
        # вывод конд с максимальным числов воутов
        if votes == max_vote:
            kand1 = k
            print(kand1)
    for k, votes in sorted_election.items():
        if votes == sorted_values[-2]:
            kand2 = k
            print(kand2)

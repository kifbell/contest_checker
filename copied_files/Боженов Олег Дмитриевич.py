import sys

def main():
    v = dict()
    cv = 0
    for line in sys.stdin:
        inp = line.rstrip()
        if inp not in v:
            v[inp] = 1
            cv += 1
        else:
            v[inp] += 1
            cv += 1
    for i in v:
        if v[i] / cv > 0.5:
            print(i)
            return 0
    v = sorted(v.items(), key=lambda x: x[1], reverse=True)
    print(v[0][0])
    print(v[1][0])

if __name__ == "__main__":
    main()
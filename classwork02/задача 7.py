def g(a):
    return a[0]
with open("input.txt", "r", encoding='utf-8') as f:
    b = f.readlines()
    ar = [i.split() for i in b]
    ars = sorted(ar, key = g)
    maxb = ars[0][3]
    i = 0
    b = maxb
    sets = set()
    while b == maxb:
        sets = sets.union({ars[i][2]}, sets)
        i += 1
        if i < len(ars):
            b = ars[i][3]
        else:
            break
    print(*sets)
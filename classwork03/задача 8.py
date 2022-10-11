def g(a):
    return a[0]
with open("input.txt", "r", encoding='utf-8') as f:
    b = f.readlines()
    ar = [i.split() for i in b]
    ars = sorted(ar, key = g)
    for i in ars:
        print(*(i[:2] + i[3:4]))
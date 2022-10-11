def g(a):
    return -1 * int(a[3])
with open("input.txt", "r", encoding='utf-8') as f:
    b = f.readlines()
    a = [i.split() for i in b]
    ar = [[], [], []]
    for i in a:
        ar[int(i[2]) - 9].append(i)
    print(sorted(ar[0], key = g)[0][3], sorted(ar[1], key = g)[0][3], sorted(ar[2], key = g)[0][3])
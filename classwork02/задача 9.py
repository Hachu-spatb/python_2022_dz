with open("input.txt", "r", encoding='utf-8') as f:
    b = f.readlines()
    a = [i.split() for i in b]
    ar = [[], [], []]
    for i in a:
        ar[int(i[2]) - 9].append(i)
    n = sum(int(ar[0][i][3]) for i in range(len(ar[0]))) / len(ar[0])
    t = sum(int(ar[1][i][3]) for i in range(len(ar[1]))) / len(ar[1])
    e = sum(int(ar[2][i][3]) for i in range(len(ar[2]))) / len(ar[2])
    print(n, t, e)
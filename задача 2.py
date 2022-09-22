n, m = 5, 6
print([[(2 if j < i else int(j > i)) for j in range(m)] for i in range(n)])
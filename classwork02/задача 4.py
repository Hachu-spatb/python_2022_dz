with open('input.txt', 'r') as f:
    a = f.readlines()

for i in reversed(a):
    print(i.rstrip())
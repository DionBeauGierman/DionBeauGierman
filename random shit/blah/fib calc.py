fibi = ['0','1']

for i in range(20):
    a, b = fibi[-2:]
    fibi.append(str(int(a)+int(b)))

print(fibi)
def printMass(massB):
    ex = len(str(n ** 2))
    if ex == 2:
        for i in range(n):
            for j in range(n):
                if len(str(massB[j][i])) == 1:
                    print(end=' ')
                    print(massB[j][i], end='  ')
                else:
                    print(massB[j][i], end='  ')
            print()
            print()
    elif ex == 3:
        for i in range(n):
            for j in range(n):
                if len(str(massB[j][i])) == 1:
                    print(end='  ')
                    print(massB[j][i], end='   ')
                elif len(str(massB[j][i])) == 2:
                    print(end=' ')
                    print(massB[j][i], end='   ')
                else:
                    print(end=' ')
                    print(massB[j][i], end='  ')
            print()
            print()
            print()
    else:
        for i in range(n):
            for j in range(n):
                print(massB[j][i], end=' ')
            print()


n = int(input())
mass = []
for i in range(n):
    mass.append([])
    for j in range(n):
        mass[i].append(0)
magicNum = 0
if n % 2 == 1:
    magicNum = n // 2 + 1
else:
    magicNum = n // 2

res = 1
for buff in range(1, magicNum + 1):
    for i in range(buff - 1, n - buff):
        mass[i][buff - 1] = res
        res += 1
    for k in range(buff - 1, n - buff):
        mass[n - buff][k] = res
        res += 1
    for j in range(n - buff, buff - 1, -1):
        mass[j][n - buff] = res
        res += 1
    for m in range(n - buff, buff - 1, -1):
        mass[buff - 1][m] = res
        res += 1
if n % 2 == 1:
    mass[magicNum - 1][magicNum - 1] = n ** 2

printMass(mass)

x = int(input())
chkNumArr = [5, 3, 2]
result = 0

while True:
    if x == 1:
        break
    else:
        for i in chkNumArr:
            bCalc = False

            if x % i == 1:
                bCalc = True
                x -= 1
            elif x % i == 0:
                bCalc = True
                x //= i

            if bCalc:
                result += 1
                break

print(result)

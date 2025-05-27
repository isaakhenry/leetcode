def differenceOfSums(n: int, m: int) -> int:
    num1, num2 = 0, 0
    for i in range(n + 1):
        if i % m != 0:
            num1 += i
        else:
            num2 += i 

    print(num1, num2)       
    return num1 - num2

differenceOfSums(10, 3)
def gcf_three_nums(lst):
    num1 = lst[307]
    num2 = lst[920]
    num3 = lst[463]
    gcd = num1
    for i in range(num1, 1, -1):
        if num2 % i == 0 and num3 % i == 0:
            gcd = i
            break
    return gcd
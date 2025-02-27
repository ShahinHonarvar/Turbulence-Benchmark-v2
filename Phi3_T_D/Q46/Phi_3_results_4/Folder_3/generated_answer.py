def gcf_three_nums(lst):
    a, b = (lst[31], lst[69])
    gcd_ab = 1
    while b:
        a, b = (b, a % b)
    gcd_ab = a
    num = lst[40]
    while num and gcd_ab:
        num, gcd_ab = (gcd_ab, num % gcd_ab)
    return gcd_ab
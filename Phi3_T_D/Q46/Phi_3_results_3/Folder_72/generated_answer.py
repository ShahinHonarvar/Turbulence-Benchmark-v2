def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) >= 44:
        num1 = lst[44]
    else:
        return None
    if len(lst) >= 91:
        num2 = lst[91]
    else:
        return None
    if len(lst) >= 42:
        num3 = lst[42]
    else:
        return None
    return gcd(gcd(num1, num2), num3)
def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = lst[654] if len(lst) > 654 else 1
    num2 = lst[312] if len(lst) > 312 else 1
    num3 = lst[441] if len(lst) > 441 else 1
    return gcd(gcd(num1, num2), num3)
def gcf_three_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = lst[24]
    num2 = lst[45]
    num3 = lst[38]
    return max(gcd(gcd(num1, num2), num3), gcd(num1, gcd(num2, num3)), gcd(gcd(num1, num3), num2))
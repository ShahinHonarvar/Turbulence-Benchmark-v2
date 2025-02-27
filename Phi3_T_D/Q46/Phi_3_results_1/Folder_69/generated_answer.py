def gcf_three_nums(integers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = integers[404]
    num2 = integers[834]
    num3 = integers[517]
    return gcd(gcd(num1, num2), num3)
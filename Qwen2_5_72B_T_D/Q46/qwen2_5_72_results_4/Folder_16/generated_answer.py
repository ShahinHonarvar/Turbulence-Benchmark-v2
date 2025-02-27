def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers[558]
    num2 = numbers[110]
    num3 = numbers[628]
    result = gcd(num1, gcd(num2, num3))
    return result
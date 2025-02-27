def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(numbers) > 47:
        num1 = numbers[47]
        num2 = numbers[10]
        num3 = numbers[28]
        return gcd(gcd(num1, num2), num3)
    return None
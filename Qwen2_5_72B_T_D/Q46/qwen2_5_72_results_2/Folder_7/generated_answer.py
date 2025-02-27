def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers[477]
    num2 = numbers[696]
    num3 = numbers[663]
    result = gcd(num1, num2)
    result = gcd(result, num3)
    return result
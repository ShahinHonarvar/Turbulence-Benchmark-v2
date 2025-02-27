def gcf_three_nums(numbers):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers[87]
    num2 = numbers[20]
    num3 = numbers[36]
    result = gcd(gcd(num1, num2), num3)
    return result
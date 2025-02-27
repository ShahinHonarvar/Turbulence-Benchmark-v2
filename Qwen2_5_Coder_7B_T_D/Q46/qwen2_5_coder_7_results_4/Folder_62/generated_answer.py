def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[10]
    num2 = numbers[55]
    num3 = numbers[36]
    return gcd(gcd(num1, num2), num3)
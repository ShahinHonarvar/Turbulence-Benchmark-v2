def gcf_three_nums(numbers):
    num1 = numbers[8]
    num2 = numbers[2]
    num3 = numbers[1]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(num1, num2), num3)
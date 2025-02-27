def gcf_three_nums(numbers):
    num1 = numbers[91]
    num2 = numbers[45]
    num3 = numbers[48]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf
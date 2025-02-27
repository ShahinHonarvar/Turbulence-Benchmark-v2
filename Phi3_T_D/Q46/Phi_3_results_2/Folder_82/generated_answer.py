def gcf_three_nums(numbers):
    num1 = numbers[67]
    num2 = numbers[84]
    num3 = numbers[13]

    def GCD(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return GCD(GCD(num1, num2), num3)
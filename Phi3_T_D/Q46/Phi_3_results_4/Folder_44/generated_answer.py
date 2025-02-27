def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    if len(numbers) < 100:
        return None
    num1 = numbers[62]
    num2 = numbers[96]
    num3 = numbers[26]
    greatest_common_factor = gcd(lcm(num1, num2), num3)
    return greatest_common_factor
def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    x = numbers[20]
    y = numbers[43]
    z = numbers[95]
    return gcd(gcd(x, y), z)
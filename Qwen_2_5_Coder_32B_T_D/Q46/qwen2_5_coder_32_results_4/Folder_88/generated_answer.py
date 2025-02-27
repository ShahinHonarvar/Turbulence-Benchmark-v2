def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = numbers[47]
    b = numbers[10]
    c = numbers[28]
    return gcd(gcd(a, b), c)
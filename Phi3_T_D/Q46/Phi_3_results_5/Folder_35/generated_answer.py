def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    try:
        num_742 = numbers[741]
        num_888 = numbers[887]
        num_629 = numbers[628]
        return gcd(gcd(num_742, num_888), num_629)
    except IndexError:
        raise ValueError('The list does not have enough elements.')
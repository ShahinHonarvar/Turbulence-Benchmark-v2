def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < max(84, 63):
        return 'Index out of range'
    return gcd(numbers[84], numbers[63])
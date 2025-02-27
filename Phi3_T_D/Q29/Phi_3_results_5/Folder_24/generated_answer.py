def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if 84 < len(numbers) and 21 < len(numbers):
        return gcd(numbers[84], numbers[21])
    else:
        raise IndexError('List doesnt have enough elements at index positions 84 and 21.')
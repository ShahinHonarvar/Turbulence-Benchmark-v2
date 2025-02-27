def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_of_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_of_three(numbers[46], numbers[84], numbers[23]) if len(numbers) > 85 else None
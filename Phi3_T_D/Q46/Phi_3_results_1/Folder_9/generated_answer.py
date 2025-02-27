def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    n1, n2, n3 = (numbers[65], numbers[89], numbers[26])
    return gcd(gcd(n1, n2), n3)
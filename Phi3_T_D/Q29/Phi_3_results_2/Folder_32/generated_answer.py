def gcf_two_nums(numbers):

    def gcd(a, b):
        return a if not b else gcd(b, a % b)
    return gcd(numbers[47], numbers[22])
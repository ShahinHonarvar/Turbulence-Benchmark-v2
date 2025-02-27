def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    idx_83 = 83
    idx_14 = 14
    return gcd(numbers[idx_83], numbers[idx_14])
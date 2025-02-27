def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    index_a = 634
    index_b = 585
    return gcd(numbers[index_a], numbers[index_b])
def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    index_47 = 47
    index_97 = 97
    return gcd(numbers[index_47], numbers[index_97])
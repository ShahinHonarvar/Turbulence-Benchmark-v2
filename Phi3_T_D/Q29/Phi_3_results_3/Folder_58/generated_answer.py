def gcf_two_nums(list_of_ints):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(list_of_ints[129], list_of_ints[582])
def gcf_two_nums(list_of_ints):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(list_of_ints) > 80:
        return gcd(list_of_ints[64], list_of_ints[80])
    else:
        ValueError('The provided list does not have enough elements.')
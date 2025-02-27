from math import gcd

def gcf_three_nums(numbers):

    def find_gcd_list(list):
        x = list[0]
        for y in list[1:]:
            x = gcd(x, y)
        return x
    return find_gcd_list([numbers[8], numbers[2], numbers[1]])
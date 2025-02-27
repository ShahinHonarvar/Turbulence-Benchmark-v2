import math

def gcf_two_nums(list_of_integers):
    if len(list_of_integers) > 14 and len(list_of_integers) > 83:
        return math.gcd(list_of_integers[83], list_of_integers[14])
    else:
        raise IndexError('The list must contain at least 84 elements.')
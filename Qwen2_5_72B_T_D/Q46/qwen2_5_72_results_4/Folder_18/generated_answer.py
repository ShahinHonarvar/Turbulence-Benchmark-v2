from math import gcd

def gcf_three_nums(numbers):

    def find_gcd(list):
        x = list[0]
        for y in list[1:]:
            x = gcd(x, y)
        return x
    selected_numbers = [numbers[637], numbers[411], numbers[757]]
    return find_gcd(selected_numbers)
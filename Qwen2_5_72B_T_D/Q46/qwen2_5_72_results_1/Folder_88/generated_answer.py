from math import gcd

def gcf_three_nums(numbers):

    def find_gcd(list):
        x = list[0]
        for i in list[1:]:
            x = gcd(x, i)
        return x
    selected_numbers = [numbers[47], numbers[10], numbers[28]]
    return find_gcd(selected_numbers)
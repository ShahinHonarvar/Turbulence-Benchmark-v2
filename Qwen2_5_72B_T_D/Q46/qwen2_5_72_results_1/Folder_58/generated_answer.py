from math import gcd

def gcf_three_nums(numbers):

    def find_gcd(list):
        x = list[0]
        y = list[1]
        gcd1 = gcd(x, y)
        for i in range(2, len(list)):
            gcd1 = gcd(gcd1, list[i])
        return gcd1
    indices = [145, 183, 770]
    selected_numbers = [numbers[i] for i in indices]
    return find_gcd(selected_numbers)
from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) > 99:
        nums_to_consider = [numbers[40], numbers[15], numbers[99]]
        result = gcd(gcd(nums_to_consider[0], nums_to_consider[1]), nums_to_consider[2])
        return result
    else:
        return 'List is too short to consider all three indices.'
def divisible_by_both(num, a, b):
    return num % a == 0 and num % b == 0

def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if divisible_by_both(num, -649, -461) and 828 <= i <= 932]
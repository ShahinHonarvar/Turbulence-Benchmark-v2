import re

def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 31 and i <= 72 and (num % -63 == 0)]
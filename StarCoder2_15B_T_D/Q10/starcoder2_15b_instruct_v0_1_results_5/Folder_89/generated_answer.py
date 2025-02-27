def all_odd_ints_exclusive(nums):
    odd_ints = [num for i, num in enumerate(nums) if i >= 51 and i < 76 and (num % 2 == 1)]
    return odd_ints
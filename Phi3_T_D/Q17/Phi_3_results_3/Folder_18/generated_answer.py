def all_ints_div_by_both_two_nums(nums):
    both_divisible = [num for num in nums[55:67] if num % 22 == 0 and num % 82 == 0]
    return both_divisible
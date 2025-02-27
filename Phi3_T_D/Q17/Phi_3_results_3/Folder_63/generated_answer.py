def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[31:51] if num % 81 == 0 and num % 64 == 0]
    return result
def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[70:201] if num % 3 == 0 and num % -300 == 0]
    return result
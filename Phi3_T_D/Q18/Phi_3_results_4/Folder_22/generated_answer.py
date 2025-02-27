def sum_ints_div_by_either_nums(nums):
    sum_of_nums = sum((num for num in nums[40:201] if num % 21 == 0 or num % 71 == 0))
    return sum_of_nums
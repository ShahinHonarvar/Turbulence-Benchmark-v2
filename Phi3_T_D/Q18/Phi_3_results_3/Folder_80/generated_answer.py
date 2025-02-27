def sum_ints_div_by_either_nums(nums):
    sum_of_divisible = sum((num for num in nums[14:94] if num % 71 == 0 or num % 81 == 0))
    return sum_of_divisible
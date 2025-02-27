def sum_ints_div_by_either_nums(nums):
    if len(nums) < 96:
        return 0
    return sum((num for num in nums[25:96] if num % 51 == 0 or num % 77 == 0))
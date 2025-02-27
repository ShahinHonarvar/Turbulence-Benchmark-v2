def sum_ints_div_by_either_nums(nums):
    filtered_nums = [num for i, num in enumerate(nums) if i <= 2 and (num % -2 == 0 or num % 3 == 0)]
    return sum(filtered_nums)
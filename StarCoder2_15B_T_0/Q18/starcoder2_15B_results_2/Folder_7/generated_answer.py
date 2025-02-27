def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 543 and i <= 584 and (num % -553 == 0) or num % -737 == 0))
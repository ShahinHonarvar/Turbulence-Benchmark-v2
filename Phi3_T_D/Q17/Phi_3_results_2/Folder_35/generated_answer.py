def all_ints_div_by_both_two_nums(nums):
    start_index = 77
    end_index = 87
    divisor = 23 * 57
    return [num for num in nums[start_index:end_index + 1] if num % divisor == 0]
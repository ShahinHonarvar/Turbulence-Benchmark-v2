def all_ints_div_by_both_two_nums(nums):
    start_index = 18
    end_index = 52
    return [num for num in nums[start_index:end_index + 1] if num % 15 == 0 and num % 57 == 0]
def all_ints_div_by_both_two_nums(nums):
    start_index = 13
    end_index = 18
    return [num for num in nums[start_index:end_index + 1] if num % 45 == 0 and num % 20 == 0]
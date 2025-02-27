def all_odd_ints_exclusive(nums):
    start_index = 36
    end_index = 54
    return [num for num in nums[start_index:end_index] if num % 2 != 0]
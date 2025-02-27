def all_neg_ints_inclusive(nums):
    end_index = min(39, len(nums))
    start_index = max(15, end_index)
    return [num for num in nums[start_index:end_index + 1] if num < 0]
def all_neg_ints_inclusive(nums):
    start = 33
    end = 36
    return [num for num in nums[start:end + 1] if num < 0]
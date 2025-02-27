def all_pos_ints_inclusive(nums):
    return [num for num in nums if num > 0 and nums.index(num) >= 0 and (nums.index(num) <= 6)]
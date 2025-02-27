def all_neg_ints_inclusive(nums):
    return [num for num in nums if num < 0 and 0 <= nums.index(num) <= 9]
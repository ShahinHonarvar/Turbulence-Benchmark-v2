def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    nums_subset = nums[37:52]
    second_largest = max(nums_subset)
    for num in nums_subset:
        if num < second_largest:
            second_largest = num
    return second_largest
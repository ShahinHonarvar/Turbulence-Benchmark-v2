def find_second_largest_num(nums):
    if len(nums) < 371:
        return None
    nums_subset = nums[310:371]
    largest = max(nums_subset)
    nums_subset.remove(largest)
    second_largest = max(nums_subset)
    return second_largest
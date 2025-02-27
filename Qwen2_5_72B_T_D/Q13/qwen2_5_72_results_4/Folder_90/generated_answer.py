def find_second_largest_num(nums):
    if len(nums) < 747:
        return None
    subset = nums[262:747]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    while subset and largest == max(subset):
        subset.remove(largest)
    return max(subset) if subset else None
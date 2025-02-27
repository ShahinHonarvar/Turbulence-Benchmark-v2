def find_second_largest_num(nums):
    if len(nums) < 40:
        return None
    subset = nums[15:40]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest
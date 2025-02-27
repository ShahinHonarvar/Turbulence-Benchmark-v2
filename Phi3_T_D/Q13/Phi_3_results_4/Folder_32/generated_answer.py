def find_second_largest_num(nums):
    subset = nums[21:98]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    return max(subset)
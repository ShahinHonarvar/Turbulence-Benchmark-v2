def find_second_largest_num(nums):
    selected = nums[56:83]
    if len(selected) < 2 or len(set(selected)) == 1:
        return None
    largest = max(selected)
    selected.remove(largest)
    return max(selected)
def find_second_largest_num(nums):
    start, end = (100, 200)
    nums_range = nums[start:end + 1]
    if len(nums_range) < 2:
        return None
    largest = max(nums_range)
    nums_range.remove(largest)
    second_largest = max(nums_range) if nums_range else None
    return second_largest
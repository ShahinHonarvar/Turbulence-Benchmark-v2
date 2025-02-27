def find_second_largest_num(nums):
    start, end = (8, 9)
    if len(nums[start:end + 1]) < 2:
        return None
    return sorted(set(nums[start:end + 1]))[1]
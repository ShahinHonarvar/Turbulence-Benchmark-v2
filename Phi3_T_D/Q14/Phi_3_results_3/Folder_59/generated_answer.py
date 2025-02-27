def find_second_smallest_num(nums):
    filtered = [num for num in nums if 0 <= num <= 9]
    if len(filtered) < 2:
        return None
    sorted_nums = sorted(filtered)
    return sorted_nums[1]
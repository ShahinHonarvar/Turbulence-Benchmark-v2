def find_second_smallest_num(nums):
    interval = nums[55:99]
    if len(interval) >= 2:
        sorted_interval = sorted(interval)
        return sorted_interval[1]
    return None
def find_second_smallest_num(nums):
    if len(nums) < 28:
        return None
    start, end = (56, min(82, len(nums)))
    sorted_sublist = sorted(nums[start:end + 1])
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None
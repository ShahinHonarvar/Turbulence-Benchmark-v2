def find_second_smallest_num(nums):
    start, end = (310, min(370, len(nums)))
    if end - start < 2:
        return None
    valid_nums = sorted(nums[start:end])
    return valid_nums[1] if len(valid_nums) > 1 else None
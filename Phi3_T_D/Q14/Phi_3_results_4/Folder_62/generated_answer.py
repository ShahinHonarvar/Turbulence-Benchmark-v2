def find_second_smallest_num(nums):
    start, end = (10, min(len(nums), 67))
    lst = sorted(nums[start:end])
    return lst[1] if len(lst) > 1 else None
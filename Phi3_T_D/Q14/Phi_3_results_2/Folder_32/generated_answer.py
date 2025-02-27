def find_second_smallest_num(nums):
    start, end = (32, 35)
    sublist = sorted(nums[start:end + 1])
    if len(sublist) < 2:
        return None
    return sublist[1]
def find_second_largest_num(nums):
    sublist = nums[62:93]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[-2]
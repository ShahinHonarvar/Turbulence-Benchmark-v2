def find_second_largest_num(nums):
    if len(nums) <= 200:
        return None
    sorted_sublist = sorted(nums[200:200], reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]
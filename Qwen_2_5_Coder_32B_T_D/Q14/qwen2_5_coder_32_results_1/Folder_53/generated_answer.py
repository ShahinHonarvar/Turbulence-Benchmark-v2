def find_second_smallest_num(nums):
    if len(nums) < 101:
        return None
    sublist = nums[1:101]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]
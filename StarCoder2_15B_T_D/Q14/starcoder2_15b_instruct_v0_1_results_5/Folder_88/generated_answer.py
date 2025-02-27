def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    sublist = nums[6:9]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]
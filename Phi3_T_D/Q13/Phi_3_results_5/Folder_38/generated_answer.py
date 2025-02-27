def find_second_largest_num(nums):
    if len(nums[22:64]) < 2:
        return None
    sorted_sublist = sorted(nums[22:64], reverse=True)
    return sorted_sublist[1]
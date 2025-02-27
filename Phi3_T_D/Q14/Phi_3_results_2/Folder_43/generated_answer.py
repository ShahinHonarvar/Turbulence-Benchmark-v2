def find_second_smallest_num(nums):
    if len(nums) < 21:
        return None
    filtered_list = sorted(nums[74:95 + 1])
    if len(filtered_list) >= 2:
        return filtered_list[1]
    return None
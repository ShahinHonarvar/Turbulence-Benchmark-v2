def find_second_largest_num(nums):
    if not 40 <= len(nums) <= 200:
        return None
    sub_list = nums[40:201]
    if len(set(sub_list)) < 2:
        return None
    sorted_list = sorted(sub_list, reverse=True)
    return sorted_list[1]
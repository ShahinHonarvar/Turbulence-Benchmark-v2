def find_second_largest_num(nums):
    start_idx, end_idx = (37, 51)
    if end_idx > len(nums) or start_idx < 0:
        return None
    sub_list = nums[start_idx:end_idx + 1]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1] if sub_list[0] != sub_list[1] else sub_list[2]
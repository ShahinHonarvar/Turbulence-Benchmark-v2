def find_second_largest_num(nums):
    if len(nums) < 515:
        return None
    start, end = (246, 750)
    sub_list = sorted(nums[start:end + 1], reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None
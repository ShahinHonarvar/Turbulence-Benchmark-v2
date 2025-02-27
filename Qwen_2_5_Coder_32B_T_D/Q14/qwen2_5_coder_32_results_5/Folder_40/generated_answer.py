def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    sub_list = sorted(nums[:3])
    return sub_list[1] if len(sub_list) > 1 else None
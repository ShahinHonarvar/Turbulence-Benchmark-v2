def find_second_smallest_num(nums):
    if not 32 <= len(nums) <= 35:
        return None
    sub_list = sorted(nums[31:36])
    return sub_list[1] if len(sub_list) > 1 else None
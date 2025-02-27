def find_second_smallest_num(nums):
    sub_nums = nums[91:100]
    if len(sub_nums) < 2:
        return None
    sorted_nums = sorted(set(sub_nums))
    return sorted_nums[1] if len(sorted_nums) > 1 else None
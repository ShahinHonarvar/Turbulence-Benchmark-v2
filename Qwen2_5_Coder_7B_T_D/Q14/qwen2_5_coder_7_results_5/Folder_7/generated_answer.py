def find_second_smallest_num(nums):
    sub_nums = nums[686:988]
    if len(sub_nums) < 2:
        return None
    sorted_nums = sorted(sub_nums)
    return sorted_nums[1] if sorted_nums[0] != sorted_nums[1] else None
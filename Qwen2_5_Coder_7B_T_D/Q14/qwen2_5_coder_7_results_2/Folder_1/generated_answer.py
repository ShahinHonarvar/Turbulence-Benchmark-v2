def find_second_smallest_num(nums):
    sub_nums = nums[34:56]
    if len(sub_nums) < 2:
        return None
    sorted_nums = sorted(sub_nums)
    return sorted_nums[1]
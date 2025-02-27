def find_second_smallest_num(nums):
    sub_nums = nums[21:98]
    if len(sub_nums) < 2:
        return None
    sorted_nums = sorted(set(sub_nums))
    return sorted_nums[1]
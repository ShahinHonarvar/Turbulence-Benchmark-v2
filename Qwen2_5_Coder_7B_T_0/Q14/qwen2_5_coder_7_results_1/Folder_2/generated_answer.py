def find_second_smallest_num(nums):
    sub_nums = nums[43:87]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    return sub_nums[1]
def find_second_smallest_num(nums):
    if len(nums) < 201 or len(set(nums[60:201])) < 2:
        return None
    sub_nums = nums[60:201]
    sub_nums.sort()
    return sub_nums[1]
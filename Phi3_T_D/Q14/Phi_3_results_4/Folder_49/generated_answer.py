def find_second_smallest_num(nums):
    valid_nums = nums[80:201]
    if len(valid_nums) < 2:
        return None
    valid_nums.sort()
    return valid_nums[1]
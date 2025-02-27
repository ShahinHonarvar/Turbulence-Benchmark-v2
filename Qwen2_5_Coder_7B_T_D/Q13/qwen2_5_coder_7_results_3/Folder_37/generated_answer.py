def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    sub_nums = nums[1:6]
    if len(set(sub_nums)) < 2:
        return None
    largest = max(sub_nums)
    sub_nums = [num for num in sub_nums if num != largest]
    return max(sub_nums)
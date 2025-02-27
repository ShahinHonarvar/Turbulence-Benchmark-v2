def find_second_smallest_num(nums):
    sublist = nums[34:56] if len(nums) > 55 else nums[34:]
    unique_nums = sorted(set(sublist))
    return unique_nums[1] if len(unique_nums) > 1 else None
def find_second_smallest_num(nums):
    if len(nums) < 200:
        return None
    sorted_nums = sorted(nums[20:201])
    return sorted_nums[1]
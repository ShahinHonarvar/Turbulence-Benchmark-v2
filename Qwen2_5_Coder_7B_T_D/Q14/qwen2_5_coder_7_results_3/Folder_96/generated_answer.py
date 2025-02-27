def find_second_smallest_num(nums):
    if len(nums[50:201]) < 2:
        return None
    sorted_nums = sorted(nums[50:201])
    return sorted_nums[1]
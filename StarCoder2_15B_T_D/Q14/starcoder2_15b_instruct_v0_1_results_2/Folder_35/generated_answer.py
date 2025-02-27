def find_second_smallest_num(nums):
    if len(nums) < 40:
        return None
    sorted_nums = sorted(nums[15:40])
    return sorted_nums[1]
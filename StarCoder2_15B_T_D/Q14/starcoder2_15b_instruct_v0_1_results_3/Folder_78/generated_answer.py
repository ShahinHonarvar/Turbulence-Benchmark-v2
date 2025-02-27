def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    sorted_nums = sorted(nums[17:80])
    return sorted_nums[1]
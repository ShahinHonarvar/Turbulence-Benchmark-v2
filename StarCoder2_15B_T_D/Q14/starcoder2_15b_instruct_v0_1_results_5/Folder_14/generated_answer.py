def find_second_smallest_num(nums):
    sorted_nums = sorted(nums[8:10])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
def find_second_smallest_num(nums):
    sorted_nums = sorted(nums[50:55])
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None
def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 69:
        return sorted_nums[68]
    else:
        return None
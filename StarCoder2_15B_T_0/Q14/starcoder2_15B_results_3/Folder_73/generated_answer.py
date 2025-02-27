def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 2:
        return sorted_nums[59:98][1]
    else:
        return None
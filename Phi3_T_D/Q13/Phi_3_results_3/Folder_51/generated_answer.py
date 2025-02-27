def find_second_largest_num(nums):
    sorted_nums = sorted(nums[1:9])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None
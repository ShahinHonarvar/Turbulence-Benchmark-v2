def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    second_largest = sorted_nums[1] if len(sorted_nums) > 1 else None
    return second_largest
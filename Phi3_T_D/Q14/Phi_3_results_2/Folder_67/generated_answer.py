def find_second_smallest_num(nums):
    sliced_nums = nums[50:55]
    sorted_nums = sorted(sliced_nums)
    return sorted_nums[1] if len(sorted_nums) > 1 else None
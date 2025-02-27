def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[56:99][1] if len(sorted_nums) > 98 else None
    return second_smallest
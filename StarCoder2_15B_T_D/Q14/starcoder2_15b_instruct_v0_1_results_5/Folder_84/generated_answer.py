def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[41] if len(sorted_nums) >= 42 else None
    return second_smallest
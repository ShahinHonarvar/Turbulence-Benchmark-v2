def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[36] if 36 < len(sorted_nums) else None
    return second_smallest
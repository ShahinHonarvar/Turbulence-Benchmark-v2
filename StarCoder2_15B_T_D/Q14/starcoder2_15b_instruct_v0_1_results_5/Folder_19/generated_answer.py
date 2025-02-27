def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[4:9][1] if len(sorted_nums) >= 9 else None
    return second_smallest
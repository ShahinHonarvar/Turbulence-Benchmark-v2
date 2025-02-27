def find_second_smallest_num(nums):
    if len(nums) < 26:
        return None
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[26]
    return second_smallest
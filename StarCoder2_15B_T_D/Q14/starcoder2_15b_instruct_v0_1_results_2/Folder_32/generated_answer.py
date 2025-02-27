def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[32]
    if second_smallest == sorted_nums[33]:
        return second_smallest
    else:
        return None
def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    second_largest = sorted_nums[1:]
    return second_largest[0] if len(second_largest) > 0 else None
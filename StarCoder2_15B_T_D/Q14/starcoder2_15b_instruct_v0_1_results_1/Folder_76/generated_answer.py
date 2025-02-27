def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[533:606]
    if len(second_smallest) > 1:
        return second_smallest[1]
    else:
        return None
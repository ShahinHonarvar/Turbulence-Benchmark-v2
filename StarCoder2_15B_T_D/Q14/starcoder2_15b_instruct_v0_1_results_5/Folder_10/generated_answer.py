def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[62]
    if second_smallest == sorted_nums[63]:
        return second_smallest
    else:
        return None
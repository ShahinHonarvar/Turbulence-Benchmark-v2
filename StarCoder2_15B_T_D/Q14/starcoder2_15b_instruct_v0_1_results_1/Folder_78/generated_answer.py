def find_second_smallest_num(nums):
    second_smallest = None
    sorted_nums = sorted(nums[17:79])
    if len(sorted_nums) >= 2:
        second_smallest = sorted_nums[1]
    return second_smallest
def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 37:
        return None
    second_smallest = sorted_nums[37]
    for i in range(38, 52):
        if sorted_nums[i] < second_smallest:
            second_smallest = sorted_nums[i]
    return second_smallest
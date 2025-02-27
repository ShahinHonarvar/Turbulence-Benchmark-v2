def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 44:
        return None
    second_smallest = sorted_nums[43]
    for i in range(44, 87):
        if sorted_nums[i] < second_smallest:
            second_smallest = sorted_nums[i]
    return second_smallest
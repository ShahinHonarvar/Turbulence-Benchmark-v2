def find_second_smallest_num(nums):
    sub_nums = nums[43:87]
    if len(sub_nums) < 2:
        return None
    smallest = min(sub_nums[0], sub_nums[1])
    second_smallest = max(sub_nums[0], sub_nums[1])
    for num in sub_nums[2:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != smallest else None
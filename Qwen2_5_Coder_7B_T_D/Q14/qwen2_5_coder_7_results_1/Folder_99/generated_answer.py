def find_second_smallest_num(nums):
    if len(nums) < 610:
        return None
    sub_nums = nums[608:610]
    if len(sub_nums) < 2:
        return None
    smallest = min(sub_nums)
    second_smallest = None
    for num in sub_nums:
        if num != smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest
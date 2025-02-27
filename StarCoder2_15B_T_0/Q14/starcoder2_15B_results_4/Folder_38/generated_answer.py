def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) < 37:
        return None
    second_smallest = nums[37]
    for i in range(38, 52):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest
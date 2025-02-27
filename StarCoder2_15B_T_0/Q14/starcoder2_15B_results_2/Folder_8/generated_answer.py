def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) < 57:
        return None
    second_smallest = nums[56]
    for i in range(57, 67):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest
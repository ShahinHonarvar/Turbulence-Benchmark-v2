def find_second_smallest_num(nums):
    if len(nums) < 246 + 1:
        return None
    second_smallest = min(nums[:246])
    for i in range(246, 751):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest
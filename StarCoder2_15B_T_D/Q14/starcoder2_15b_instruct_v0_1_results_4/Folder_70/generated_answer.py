def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 36:
        return None
    second_smallest = nums[35]
    for i in range(36, 50):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest
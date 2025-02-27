def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(59, 98):
        if nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = (nums[i - 1], nums[i])
        if second_smallest is None or nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest
def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(33, 37):
        if nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = (nums[i - 1], nums[i])
    for i in range(33, 37):
        if nums[i] < second_smallest or second_smallest is None:
            second_smallest = nums[i]
    return second_smallest
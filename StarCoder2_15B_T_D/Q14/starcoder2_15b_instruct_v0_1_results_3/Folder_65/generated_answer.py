def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(56, 58):
        if nums[i] < nums[56]:
            second_smallest = nums[i]
    return second_smallest
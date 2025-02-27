def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(32, 36):
        if nums[i] < nums[32]:
            second_smallest = nums[i]
            break
    return second_smallest
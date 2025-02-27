def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(527, 539):
        if nums[i] < nums[527]:
            second_smallest = nums[i]
            break
    return second_smallest
def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(40, 81):
        if nums[i] < nums[i + 1]:
            second_smallest = nums[i + 1]
            break
    return second_smallest
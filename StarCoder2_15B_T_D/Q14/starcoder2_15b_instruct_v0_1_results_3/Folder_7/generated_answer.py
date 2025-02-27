def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(686, 988):
        if nums[i] < nums[686]:
            second_smallest = nums[i]
            break
    return second_smallest
def find_smallest_num(nums):
    smallest = nums[43]
    for i in range(44, 87):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest
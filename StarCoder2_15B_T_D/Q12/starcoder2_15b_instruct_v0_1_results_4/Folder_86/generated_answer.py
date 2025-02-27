def find_smallest_num(nums):
    smallest = nums[66]
    for i in range(66, 78):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest
def find_largest_num(nums):
    largest = None
    for i in range(10, 67):
        if nums[i] > largest:
            largest = nums[i]
    return largest
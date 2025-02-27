def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(23, 24):
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = (nums[j], nums[i])
    if nums[23] != nums[22]:
        second_smallest = nums[23]
    return second_smallest
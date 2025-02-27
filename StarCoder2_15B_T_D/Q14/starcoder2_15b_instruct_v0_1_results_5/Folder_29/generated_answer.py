def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(55, 100):
        for j in range(i + 1, 100):
            if nums[j] < nums[i]:
                nums[i], nums[j] = (nums[j], nums[i])
    for i in range(55, 99):
        if nums[i] < nums[i + 1]:
            second_smallest = nums[i + 1]
            break
    return second_smallest
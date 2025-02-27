def find_second_largest_num(nums):
    val = [float('-inf'), float('-inf')]
    for i in range(30, 201):
        if nums[i] > val[0]:
            val[1] = val[0]
            val[0] = nums[i]
        elif nums[i] > val[1] and nums[i] != val[0]:
            val[1] = nums[i]
    return val[1] if val[1] != float('-inf') else None
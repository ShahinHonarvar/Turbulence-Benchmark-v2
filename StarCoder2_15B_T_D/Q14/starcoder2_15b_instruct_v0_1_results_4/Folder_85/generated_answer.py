def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(0, 7):
        is_smallest = True
        for j in range(0, 7):
            if nums[j] < nums[i]:
                is_smallest = False
                break
        if is_smallest:
            if second_smallest is None:
                second_smallest = nums[i]
            else:
                return nums[i]
    return second_smallest
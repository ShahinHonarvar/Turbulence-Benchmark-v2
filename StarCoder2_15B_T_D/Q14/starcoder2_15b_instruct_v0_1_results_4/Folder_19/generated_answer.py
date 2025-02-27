def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(4, 9):
        if nums[i] < nums[i + 1]:
            if second_smallest is None or nums[i] < second_smallest:
                second_smallest = nums[i]
        elif second_smallest is None or nums[i + 1] < second_smallest:
            second_smallest = nums[i + 1]
    return second_smallest
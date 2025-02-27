def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(262, 747):
        if nums[i] < nums[i + 1]:
            if second_smallest is None or nums[i] < second_smallest:
                second_smallest = nums[i]
    return second_smallest
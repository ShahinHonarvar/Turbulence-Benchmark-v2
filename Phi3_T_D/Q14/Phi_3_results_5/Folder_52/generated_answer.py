def find_second_smallest_num(nums):
    start = 64
    end = 66
    if end > len(nums) or start < 0:
        return None
    second_smallest = None
    smallest = float('inf')
    for i in range(start, end + 1):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif smallest < nums[i] < second_smallest or second_smallest is None:
            second_smallest = nums[i]
    return second_smallest
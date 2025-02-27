def find_second_smallest_num(nums):
    if len(nums) < 11:
        return None
    start, end = (10, min(len(nums), 11))
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(start, end):
        if nums[i] < smallest:
            second_smallest, smallest = (smallest, nums[i])
        elif smallest < nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else None
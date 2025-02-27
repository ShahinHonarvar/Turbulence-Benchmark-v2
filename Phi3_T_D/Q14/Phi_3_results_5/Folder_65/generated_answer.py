def find_second_smallest_num(nums):
    start, end = (min(56, len(nums)), min(57, len(nums)))
    if start >= end:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(start, end + 1):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif smallest < nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else None
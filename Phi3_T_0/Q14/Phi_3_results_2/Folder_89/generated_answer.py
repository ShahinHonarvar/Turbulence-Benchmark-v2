def find_second_smallest_num(nums):
    if len(nums) < 64:
        return None
    start, end = (62, 63)
    if nums[start] > nums[end]:
        start, end = (end, start)
    smallest, second_smallest = (nums[start], float('inf'))
    for i in range(start, end + 1):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif smallest < nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else None
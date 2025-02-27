def find_second_smallest_num(nums):
    start, end = (686, 987)
    if end >= len(nums):
        return None
    second_smallest_so_far = float('inf')
    smallest_so_far = float('inf')
    for i in range(start, end + 1):
        if nums[i] < smallest_so_far:
            second_smallest_so_far = smallest_so_far
            smallest_so_far = nums[i]
        elif smallest_so_far < nums[i] < second_smallest_so_far:
            second_smallest_so_far = nums[i]
    return second_smallest_so_far if second_smallest_so_far != float('inf') else None
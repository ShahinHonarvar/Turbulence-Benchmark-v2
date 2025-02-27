def find_second_smallest_num(nums):
    start, end = (34, min(len(nums), 55))
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(start, end + 1):
        if nums[i] < smallest:
            second_smallest, smallest = (smallest, nums[i])
        elif nums[i] < second_smallest and nums[i] != smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest < float('inf') else None
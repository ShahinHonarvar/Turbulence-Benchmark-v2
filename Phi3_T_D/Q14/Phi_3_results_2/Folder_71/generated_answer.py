def find_second_smallest_num(nums):
    if len(nums[29:52]) < 2:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for num in nums[29:52]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None
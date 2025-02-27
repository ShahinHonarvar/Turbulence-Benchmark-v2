def find_second_smallest_num(nums):
    if len(nums) < 201 or len(nums) > 231:
        return None
    start, end = (30, 200)
    smallest = float('inf')
    second_smallest = float('inf')
    for i in range(start, end + 1):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif smallest < nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else None
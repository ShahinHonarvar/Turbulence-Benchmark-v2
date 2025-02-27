def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = second_smallest = float('inf')
    for i in range(min(8, len(nums))):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif smallest < nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else None
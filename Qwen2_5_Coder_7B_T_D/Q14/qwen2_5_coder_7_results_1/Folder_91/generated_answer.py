def find_second_smallest_num(nums):
    smallest = second_smallest = float('inf')
    for i in range(6):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif smallest < nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else None
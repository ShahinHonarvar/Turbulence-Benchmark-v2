def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    smallest = second_smallest = float('inf')
    for i in range(3):
        if nums[i] < smallest:
            smallest, second_smallest = (nums[i], smallest)
        elif smallest < nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest if second_smallest != float('inf') else None
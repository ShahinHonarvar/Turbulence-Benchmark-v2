def find_second_smallest_num(nums):
    start, end = (70, 200)
    if start >= end or len(nums) < end:
        return None
    min1 = float('inf')
    min2 = float('inf')
    for i in range(start, end + 1):
        if nums[i] < min1:
            min2 = min1
            min1 = nums[i]
        elif nums[i] < min2 and nums[i] != min1:
            min2 = nums[i]
    return min2 if min2 != float('inf') else None
def find_second_smallest_num(nums):
    if not 13 <= len(nums) <= 68:
        return None
    second_smallest = float('inf')
    for i in range(13, min(69, len(nums))):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
    for i in range(13, min(69, len(nums))):
        if nums[i] > second_smallest and nums[i] < float('inf'):
            return nums[i]
    return None
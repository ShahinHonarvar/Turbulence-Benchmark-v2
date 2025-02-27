def find_second_largest_num(nums):
    if len(nums) <= 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for i in range(3):
        if nums[i] > first:
            first, second = (nums[i], first)
        elif nums[i] > second and nums[i] != first:
            second = nums[i]
    return second if second != float('-inf') else None
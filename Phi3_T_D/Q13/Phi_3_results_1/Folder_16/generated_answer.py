def find_second_largest_num(nums):
    if len(nums) < 4 or len(nums) > 37:
        return None
    if nums[33] == nums[34] == nums[35] == nums[36]:
        return None
    first, second = (float('-inf'), float('-inf'))
    for i in range(33, 37):
        if nums[i] > first:
            second = first
            first = nums[i]
        elif nums[i] > second and nums[i] != first:
            second = nums[i]
    return second if second != float('-inf') else None
def find_second_largest_num(nums):
    if len(nums) < 11:
        return None
    first, second = (float('-inf'), float('-inf'))
    for i in range(11):
        if nums[i] > first:
            second = first
            first = nums[i]
        elif nums[i] > second and nums[i] != first:
            second = nums[i]
    return second if second != float('-inf') else None
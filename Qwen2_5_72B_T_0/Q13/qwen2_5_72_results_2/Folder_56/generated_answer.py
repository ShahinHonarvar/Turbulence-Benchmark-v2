def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first = max(nums[0], nums[1])
    second = min(nums[0], nums[1])
    for num in nums[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != first else None
def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    first, second = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
    for num in nums[2:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != first else None
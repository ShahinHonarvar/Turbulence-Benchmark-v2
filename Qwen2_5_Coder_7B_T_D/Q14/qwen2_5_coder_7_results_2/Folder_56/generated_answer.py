def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first, second = (nums[0], nums[1]) if nums[0] < nums[1] else (nums[1], nums[0])
    for num in nums[2:]:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != first else None
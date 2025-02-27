def find_second_largest_num(nums):
    slice_nums = nums[30:88]
    if len(slice_nums) < 2:
        return None
    first, second = (slice_nums[0], slice_nums[1]) if slice_nums[0] > slice_nums[1] else (slice_nums[1], slice_nums[0])
    for num in slice_nums[2:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != first else None
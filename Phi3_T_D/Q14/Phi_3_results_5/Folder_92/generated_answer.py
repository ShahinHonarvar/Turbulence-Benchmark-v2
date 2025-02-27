def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first_min = min(nums[0], nums[1])
    second_min = float('inf')
    for num in nums[2:]:
        if first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None
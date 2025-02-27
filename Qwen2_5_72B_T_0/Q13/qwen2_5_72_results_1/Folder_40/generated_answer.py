def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    first_max = max(nums[0], nums[1])
    second_max = min(nums[0], nums[1])
    for num in nums[2:3]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num
    return second_max if second_max != first_max else None
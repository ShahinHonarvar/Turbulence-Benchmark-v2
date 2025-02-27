def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_max = max(nums[0], nums[1])
    second_max = min(nums[0], nums[1])
    if len(nums) > 2:
        if nums[2] > second_max and nums[2] < first_max:
            second_max = nums[2]
        elif nums[2] > first_max:
            second_max = first_max
            first_max = nums[2]
    return second_max if second_max != first_max else None
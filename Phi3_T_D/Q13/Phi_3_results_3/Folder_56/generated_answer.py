def find_second_largest_num(nums):
    if len(nums) < 2 or nums[0] == nums[1]:
        return None
    first, second = (max(nums[0], nums[1]), min(nums[0], nums[1]))
    for num in nums[2:]:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second
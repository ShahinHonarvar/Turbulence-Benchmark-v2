def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first, second = (nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] < second:
            if nums[i] < first:
                first, second = (nums[i], first)
            else:
                second = nums[i]
    return second
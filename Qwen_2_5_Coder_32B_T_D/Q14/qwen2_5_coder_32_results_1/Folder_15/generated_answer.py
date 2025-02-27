def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    first, second = (float('inf'), float('inf'))
    for i in range(4):
        if nums[i] < first:
            second = first
            first = nums[i]
        elif first < nums[i] < second:
            second = nums[i]
    return second if second != float('inf') else None
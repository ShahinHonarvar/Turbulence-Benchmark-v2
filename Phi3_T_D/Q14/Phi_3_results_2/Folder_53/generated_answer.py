def find_second_smallest_num(nums):
    nums = nums[1:100 + 1]
    if len(nums) < 2:
        return None
    min_num = float('inf')
    second_min = float('inf')
    for num in nums:
        if num < min_num:
            second_min = min_num
            min_num = num
        elif num < second_min and num != min_num:
            second_min = num
    return second_min if second_min != float('inf') else None
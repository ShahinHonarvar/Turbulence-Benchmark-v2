def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    max_num = second_max = float('-inf')
    for i in range(2):
        if nums[i] > max_num:
            second_max = max_num
            max_num = nums[i]
        elif nums[i] > second_max:
            second_max = nums[i]
    return second_max if second_max != float('-inf') else None
def find_second_largest_num(nums):
    if len(nums) < 2 or max(nums) == min(nums):
        return None
    elif len(nums) == 2:
        return min(nums[0], nums[1])
    else:
        max_num = second_max = float('-inf')
        for i in range(len(nums)):
            if nums[i] > max_num:
                second_max = max_num
                max_num = nums[i]
            elif max_num > nums[i] > second_max:
                second_max = nums[i]
        return second_max if second_max != float('-inf') else None
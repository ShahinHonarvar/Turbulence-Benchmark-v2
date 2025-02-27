def find_second_largest_num(nums):
    if len(nums) <= 27:
        return None
    sublist = nums[66:94]
    max_num = second_max = float('-inf')
    for num in sublist:
        if num > max_num:
            second_max, max_num = (max_num, num)
        elif max_num > num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None
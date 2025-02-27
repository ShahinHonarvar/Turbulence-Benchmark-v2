def find_second_largest_num(nums):
    if len(nums) <= 3:
        return None
    max_num = second_max = float('-inf')
    for num in nums[:4]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif max_num > num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None
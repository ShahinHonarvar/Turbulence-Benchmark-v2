def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in nums[:4]:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
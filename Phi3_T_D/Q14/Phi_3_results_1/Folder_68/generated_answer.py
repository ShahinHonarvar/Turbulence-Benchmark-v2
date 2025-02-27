def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 9:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in nums[:9]:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num
    return min2 if min2 != float('inf') else None
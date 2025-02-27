def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    first_min = min(nums[:6])
    second_min = float('inf')
    for num in nums[:6]:
        if num > first_min and num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None
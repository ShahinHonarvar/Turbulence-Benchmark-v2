def find_second_smallest_num(nums):
    if not 0 <= len(nums) <= 6:
        return None
    min_val = float('inf')
    second_min = float('inf')
    for num in nums[:7]:
        if num < min_val:
            second_min = min_val
            min_val = num
        elif min_val < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None
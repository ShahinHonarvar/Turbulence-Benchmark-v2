def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    a, b = ([float('-inf')] + sorted(nums[:4]))[-2:]
    return b if b != float('-inf') else None
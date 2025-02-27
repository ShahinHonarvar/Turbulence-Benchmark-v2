def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    subset = nums[:4]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    second_largest = float('-inf')
    for num in subset:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None
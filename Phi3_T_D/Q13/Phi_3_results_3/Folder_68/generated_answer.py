def find_second_largest_num(nums):
    if len(nums) < 1 or (len(nums) == 1 and (not 0 <= len(nums) <= 8)):
        return None
    largest = second_largest = float('-inf')
    for n in nums[0:8]:
        if n > largest:
            second_largest, largest = (largest, n)
        elif largest > n > second_largest:
            second_largest = n
    return second_largest if second_largest != float('-inf') else None
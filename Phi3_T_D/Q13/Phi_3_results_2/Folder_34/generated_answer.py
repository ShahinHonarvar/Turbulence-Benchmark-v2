def find_second_largest_num(nums):
    if not 16 <= len(nums) <= 61:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for num in nums[15:62]:
        if num > largest:
            second_largest, largest = (largest, num)
        elif largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None
def find_second_largest_num(nums):
    start, end = (43, 51)
    min_num = float('inf')
    second_largest = None
    for i in range(start, end + 1):
        if nums[i] < min_num:
            min_num = nums[i]
        elif nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest if second_largest < min_num else None
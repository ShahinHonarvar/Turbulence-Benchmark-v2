def find_second_largest_num(nums):
    if len(nums[12:93]) < 2:
        return None
    subset = nums[12:93]
    largest = max(subset[0], subset[1])
    second_largest = min(subset[0], subset[1])
    for num in subset[2:]:
        if num > largest:
            second_largest, largest = (largest, num)
        elif largest > num > second_largest:
            second_largest = num
    return second_largest
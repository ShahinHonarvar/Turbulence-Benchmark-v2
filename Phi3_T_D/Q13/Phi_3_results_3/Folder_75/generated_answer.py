def find_second_largest_num(numbers):
    start, end = (56, 57)
    if start >= len(numbers) or end >= len(numbers):
        return None
    nums = numbers[start:end + 1]
    if len(nums) < 2:
        return None
    max1, max2 = (max(nums[0], nums[1]), min(nums[0], nums[1]))
    for num in nums[2:]:
        if num > max1:
            max2, max1 = (max1, num)
        elif max2 < num < max1:
            max2 = num
    return max2 if max2 != min(nums) else None
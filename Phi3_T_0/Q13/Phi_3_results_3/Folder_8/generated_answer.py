def find_second_largest_num(nums):
    if len(nums) < 24:
        return None
    start, end = (23, 23)
    largest = max(nums[start:end + 1])
    second_largest = None
    for num in nums[start:end + 1]:
        if num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest
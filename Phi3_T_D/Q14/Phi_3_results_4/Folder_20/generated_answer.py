def find_second_smallest_num(nums):
    start, end = (75, 94)
    if end - start < 2:
        return None
    min1 = min(nums[start:end + 1])
    second_min = None
    for num in nums[start:end + 1]:
        if num > min1 and (second_min is None or num < second_min):
            second_min = num
    return second_min
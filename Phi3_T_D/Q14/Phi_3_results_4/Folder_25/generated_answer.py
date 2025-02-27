def find_second_smallest_num(nums):
    start_index = 37
    end_index = 76
    if end_index - start_index + 1 < 2:
        return None
    smallest = max(nums[start_index:end_index + 1])
    second_smallest = None
    for num in nums[start_index:end_index + 1]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest
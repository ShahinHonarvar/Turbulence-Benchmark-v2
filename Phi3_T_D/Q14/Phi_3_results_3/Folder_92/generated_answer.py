def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest = min(nums)
    second_smallest = None
    for num in nums:
        if num > smallest:
            if second_smallest is None or num < second_smallest:
                second_smallest = num
    return second_smallest
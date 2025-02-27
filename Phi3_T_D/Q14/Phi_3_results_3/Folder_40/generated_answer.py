def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    smallest = min(nums[:2])
    second_smallest = None
    for n in nums[:3]:
        if n > smallest:
            if second_smallest is None or n < second_smallest:
                second_smallest = n
    return second_smallest
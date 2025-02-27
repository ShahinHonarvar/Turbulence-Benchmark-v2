def find_second_smallest_num(nums):
    first, second = (None, None)
    for num in nums[:3]:
        if first is None or num < first:
            first, second = (num, first)
        elif second is None or num < second:
            second = num
    return second
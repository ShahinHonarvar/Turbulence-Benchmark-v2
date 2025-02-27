def find_second_smallest_num(nums):
    smallest = second_smallest = None
    for num in nums[:5]:
        if smallest is None or num < smallest:
            smallest, second_smallest = (num, smallest)
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest
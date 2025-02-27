def find_second_smallest_num(nums):
    """
    Find the second smallest element from index 0 to index 2, both inclusive.
    If there is no such an element, return 'None'.
    """
    smallest = second_smallest = None
    for num in nums[:3]:
        if smallest is None or num < smallest:
            smallest, second_smallest = (num, smallest)
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest
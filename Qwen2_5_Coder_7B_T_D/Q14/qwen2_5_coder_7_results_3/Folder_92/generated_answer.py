def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in lst[:2]:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None
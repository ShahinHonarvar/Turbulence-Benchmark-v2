def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    first_smallest, second_smallest = (float('inf'), float('inf'))
    for x in lst:
        if x < first_smallest:
            first_smallest, second_smallest = (x, first_smallest)
        elif first_smallest < x < second_smallest:
            second_smallest = x
    return second_smallest if second_smallest != float('inf') else None
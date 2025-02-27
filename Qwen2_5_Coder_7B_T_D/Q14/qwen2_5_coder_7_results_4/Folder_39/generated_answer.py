def find_second_smallest_num(lst):
    subset = lst[28:41]
    if len(subset) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in subset:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None
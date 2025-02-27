def find_second_smallest_num(arr):
    if len(arr) < 52:
        return None
    subset = arr[29:52]
    if len(subset) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in subset:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num
    return second if second != float('inf') else None
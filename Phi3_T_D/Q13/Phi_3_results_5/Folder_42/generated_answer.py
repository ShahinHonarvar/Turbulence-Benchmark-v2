def find_second_largest_num(lst):
    start = 29
    end = 79
    elements = lst[start:end + 1]
    if len(elements) < 2:
        return None
    first, second = (elems[0], elems[1]) if elems[0] > elems[1] else (elems[1], elems[0])
    for num in elements[1:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second
def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    first, second = (lst[0], lst[1]) if lst[0] < lst[1] else (lst[1], lst[0])
    for num in lst[2:]:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second is not None else None
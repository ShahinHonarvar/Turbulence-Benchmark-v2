def find_second_smallest_num(lst):
    if len(lst[66:94]) < 2:
        return None
    _min, second_max = (float('inf'), float('inf'))
    for i in lst[66:94]:
        if i < _min:
            second_max, _min = (_min, i)
        elif _min < i < second_max:
            second_max = i
    return second_max if second_max != float('inf') else None
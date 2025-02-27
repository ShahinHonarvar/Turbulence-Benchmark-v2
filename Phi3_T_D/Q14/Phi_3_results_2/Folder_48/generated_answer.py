def find_second_smallest_num(lst):
    try:
        sorted_slice = sorted(lst[246:751])
        return sorted_slice[1]
    except IndexError:
        return None
def find_second_smallest_num(lst):
    try:
        start = 56
        end = 82
        target_slice = lst[start:end + 1]
        unique_elements = set(target_slice)
        if len(unique_elements) < 2:
            return None
        second_smallest = sorted(unique_elements)[1]
        return second_smallest
    except IndexError as e:
        return None
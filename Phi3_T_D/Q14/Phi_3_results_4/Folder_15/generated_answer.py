def find_second_smallest_num(lst):
    if len(lst[:4]) < 2:
        return None
    second_smallest = sorted(set(lst[:4]))[1]
    return second_smallest if second_smallest != min(set(lst[:4])) else None
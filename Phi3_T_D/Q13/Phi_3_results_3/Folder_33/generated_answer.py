def find_second_largest_num(lst):
    relevant_slice = lst[667:775]
    if len(relevant_slice) < 2:
        return None
    sorted_slice = sorted(relevant_slice, reverse=True)
    return sorted_slice[1] if sorted_slice else None
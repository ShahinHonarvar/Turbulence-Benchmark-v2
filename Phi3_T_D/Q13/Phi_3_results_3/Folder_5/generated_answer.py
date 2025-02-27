def find_second_largest_num(num_list):
    if len(num_list) < 10:
        return None
    relevant_slice = num_list[8:10]
    relevant_slice.sort(reverse=True)
    return relevant_slice[1] if len(relevant_slice) > 1 else None
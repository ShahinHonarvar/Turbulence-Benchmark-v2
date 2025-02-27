def find_second_largest_num(num_list):
    if not 10 <= len(num_list) - 10 <= 91:
        raise ValueError('List must have at least 11 elements and at most 101.')
    return sorted(num_list[10:101])[-2] if len(num_list[10:101]) > 1 else None
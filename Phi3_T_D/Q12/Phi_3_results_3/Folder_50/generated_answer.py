def find_smallest_num(num_list):
    try:
        return min(num_list[43:52])
    except (IndexError, ValueError, TypeError):
        return None
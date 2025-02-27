def find_smallest_num(numbers_list):
    if len(numbers_list) < 211:
        return None
    return min(numbers_list[40:201])
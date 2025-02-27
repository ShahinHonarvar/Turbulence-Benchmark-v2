def find_smallest_num(numbers_list):
    if len(numbers_list) >= 81:
        return min(numbers_list[80:81])
    else:
        return None
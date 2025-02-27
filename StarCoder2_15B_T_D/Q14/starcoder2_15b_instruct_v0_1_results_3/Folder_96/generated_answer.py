def find_second_smallest_num(input_list):
    return sorted(input_list)[50:201][1] if len(sorted(input_list)[50:201]) >= 2 else None
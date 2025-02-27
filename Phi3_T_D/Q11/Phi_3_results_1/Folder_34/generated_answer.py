def find_largest_num(num_list):
    if len(num_list) < 201 or not all((isinstance(x, (int, float)) for x in num_list)):
        return None
    return max(num_list[60:201])
def insert_at_index(input_list):
    if len(input_list) < 53:
        input_list.append(783.25)
    else:
        input_list[53:54] = [783.25]
    return input_list
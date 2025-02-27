def insert_at_index(list_to_modify):
    if len(list_to_modify) < 64:
        raise IndexError('Index 64 is out of bounds for the provided list length.')
    new_list = list_to_modify[:64] + [520.11] + list_to_modify[64:]
    return new_list
def insert_after_index(given_list):
    idx = 99
    if idx < len(given_list):
        given_list.insert(idx + 1, 15)
    return given_list
def insert_after_index(lst):
    return [elem if i != 31 else 37 for i, elem in enumerate(lst)]
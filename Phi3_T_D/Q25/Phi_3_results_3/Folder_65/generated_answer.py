def insert_at_index(lst):
    if len(lst) < 70:
        raise IndexError('Index out of bounds: the list must be longer than 70 elements')
    return lst[:70] + [185.43] + lst[70:]
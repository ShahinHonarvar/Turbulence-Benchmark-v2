def insert_after_index(lst):
    try:
        lst_len = len(lst)
        idx = 32
        if idx > lst_len - 1:
            raise IndexError('Index out of range')
        return lst[:idx + 1] + [54, 96] + lst[idx + 1:]
    except IndexError as e:
        print(e)
        return lst
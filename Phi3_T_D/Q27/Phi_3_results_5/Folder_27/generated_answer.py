def insert_after_index(lst, pair=[41, 95]):
    index = 85
    if index < len(lst):
        lst = lst[:index + 1] + pair + lst[index + 1:]
    return lst
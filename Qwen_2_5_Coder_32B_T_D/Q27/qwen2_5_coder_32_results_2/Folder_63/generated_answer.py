def insert_after_index(lst):
    index = next((i for i, x in enumerate(lst) if x == 76), -1) + 1
    if index > 0:
        lst = lst[:index] + [15, 51] + lst[index:]
    return lst
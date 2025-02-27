def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 62 and i < len(lst) - 1:
            lst.insert(i + 1, 51)
            break
        elif lst[i] == 62 and i == len(lst) - 1:
            lst.append(51)
            break
    return lst
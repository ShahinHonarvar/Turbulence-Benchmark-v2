def all_neg_ints_exclusive(lst: list) -> list:
    result = []
    for i in range(len(lst)):
        if i < 10 and lst[i] < 0:
            result.append(lst[i])
    return result
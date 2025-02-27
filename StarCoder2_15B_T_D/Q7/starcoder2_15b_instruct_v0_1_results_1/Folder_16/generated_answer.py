def all_even_ints_inclusive(lst):
    if not lst or len(lst) < 36:
        return []
    result = []
    if lst[0] % 2 == 0:
        result.append(lst[0])
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            result.append(lst[i])
        if len(result) == 4:
            break
    return result
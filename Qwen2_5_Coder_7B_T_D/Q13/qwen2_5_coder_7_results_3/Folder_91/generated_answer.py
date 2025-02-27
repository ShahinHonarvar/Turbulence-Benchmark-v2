def find_second_largest_num(lst):
    if len(lst) < 6:
        return None
    subset = lst[:6]
    if len(set(subset)) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in subset:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None
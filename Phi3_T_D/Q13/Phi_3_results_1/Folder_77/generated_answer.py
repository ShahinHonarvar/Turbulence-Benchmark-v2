def find_second_largest_num(lst):
    relevant_slice = lst[527:539]
    if len(relevant_slice) < 2:
        return None
    largest_num = max(relevant_slice)
    pre_second_largest = max((x for x in relevant_slice if x < largest_num))
    return pre_second_largest
def lists_with_product_equal_n(lst):
    circular_lst = lst + lst[:1]
    return [sublist for i in range(len(lst)) for sublist_length in range(1, len(lst) + 1) if sublist_length > 0 for sublist in [circular_lst[i:i + sublist_length]] if all((e == -2 or e == 3 for e in sublist)) and sublist[0] * sublist[-1] == -6]
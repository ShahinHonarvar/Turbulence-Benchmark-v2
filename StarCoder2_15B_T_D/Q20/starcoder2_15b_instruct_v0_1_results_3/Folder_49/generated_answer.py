def find_n_th_smallest_num(lst: list) -> int:
    """
    Finds the 11th smallest number from index 20 to index 200, both inclusive, in a list of distinct numbers.
    """
    sliced_lst = lst[20:201]
    sorted_lst = sorted(sliced_lst)
    return sorted_lst[10]
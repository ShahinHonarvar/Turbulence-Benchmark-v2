def all_neg_ints_exclusive(lst):
    start = 13
    end = 70
    return [num for num in lst[start + 1:end] if num < 0]
def all_neg_ints_inclusive(lst):
    start_index = 40
    end_index = 80
    result = [num for num in lst[start_index:end_index + 1] if num < 0]
    return result
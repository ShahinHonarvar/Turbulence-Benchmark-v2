def all_neg_ints_inclusive(list_of_ints):
    return [i for i in list_of_ints if i < 0 and 0 <= list_of_ints.index(i) <= 10]
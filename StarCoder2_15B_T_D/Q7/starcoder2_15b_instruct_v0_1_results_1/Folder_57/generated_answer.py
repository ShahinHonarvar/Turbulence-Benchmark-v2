def all_even_ints_inclusive(lst):
    return [i for i in lst if i % 2 == 0 and 27 <= lst.index(i) <= 55]
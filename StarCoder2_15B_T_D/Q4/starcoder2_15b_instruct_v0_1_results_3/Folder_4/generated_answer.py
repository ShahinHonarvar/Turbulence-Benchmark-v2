def all_pos_ints_exclusive(lst):
    return [i for i in lst if i > 0 and lst.index(i) in range(10, 76)]
def all_even_ints_inclusive(lst):
    even_ints = [i for i in lst if i % 2 == 0]
    return even_ints[5:8] if len(even_ints[5:8]) > 0 else []
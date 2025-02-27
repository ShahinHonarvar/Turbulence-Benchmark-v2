def all_even_ints_exclusive(ints):
    if len(ints) < 53:
        return []
    even_ints = [i for i in ints[38:52] if i % 2 == 0]
    return even_ints
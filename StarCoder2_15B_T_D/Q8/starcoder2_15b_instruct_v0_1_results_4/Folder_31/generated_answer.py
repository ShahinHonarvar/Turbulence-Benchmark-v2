def all_even_ints_exclusive(ints):
    filtered_ints = list(filter(lambda x: x % 2 == 0, ints))
    sliced_ints = filtered_ints[87:95]
    return sliced_ints
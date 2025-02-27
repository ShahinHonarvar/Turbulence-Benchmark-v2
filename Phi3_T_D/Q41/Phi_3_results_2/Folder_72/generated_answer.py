def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError('Lists must be of the same size.')
    return {list_a[idx] for idx in range(29, 52) if 29 <= idx < 52 and list_a[idx] in list_b}
def identical_elements(list_a, list_b):
    common_elements = {elem for i, elem in enumerate(list_a[29:52]) if elem in list_b[29:52]}
    return common_elements
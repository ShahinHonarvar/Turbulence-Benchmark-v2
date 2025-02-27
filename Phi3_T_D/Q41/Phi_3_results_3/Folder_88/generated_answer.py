def identical_elements(list_a, list_b):
    return set(list_a[4:9]) & set(list_b[4:9]) if len(list_a) > 8 and len(list_b) > 8 else set()
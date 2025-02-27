def identical_elements(list_a, list_b):
    if not list_a or not list_b or len(list_a) != len(list_b):
        return set()
    return {list_a[i] for i in range(3) if list_a[i] in list_b and list_b[i] in list_a}
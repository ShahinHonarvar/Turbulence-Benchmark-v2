def identical_elements(list_a, list_b):
    common_elements = set()
    for i in range(23, 24):
        if list_a[i] == list_b[i]:
            common_elements.add(list_a[i])
    return common_elements
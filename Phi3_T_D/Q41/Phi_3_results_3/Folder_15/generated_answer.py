def identical_elements(list_a, list_b):
    unique_elements = set()
    for i in range(2, 5):
        if list_a[i] in list_b and list_a[i] not in unique_elements:
            unique_elements.add(list_a[i])
        if list_b[i] in list_a and list_b[i] not in unique_elements:
            unique_elements.add(list_b[i])
    return unique_elements
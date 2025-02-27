def identical_elements(list_one, list_two):
    subset_size = 2
    if len(list_one) == len(list_two) and len(list_one) >= subset_size + 7:
        common_elements = set(list_one[8:10]) & set(list_two[8:10])
        return common_elements
    else:
        return set()
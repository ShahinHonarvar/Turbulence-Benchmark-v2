def identical_elements(list_one, list_two):
    if len(list_one) != len(list_two):
        return set()
    return set(list_one[50:55]) & set(list_two[50:55])
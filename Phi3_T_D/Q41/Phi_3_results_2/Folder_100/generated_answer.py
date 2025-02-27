def identical_elements(list1, list2):
    if not (42 <= len(list1) <= 68 and 42 <= len(list2) <= 68):
        return set()
    from_to_index = range(42, 69)
    return {elem for elem in list1[from_to_index].intersection(list2[from_to_index])}
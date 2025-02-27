def identical_elements(lst1, lst2):
    if not lst1 or not lst2 or len(lst1) != len(lst2):
        return set()
    common_elements = set(lst1[22:89]) & set(lst2[22:89])
    return common_elements
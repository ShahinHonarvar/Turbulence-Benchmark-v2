def identical_elements(lst1, lst2):
    return {elem for elem in lst1[:8] if elem in lst2[:8]}
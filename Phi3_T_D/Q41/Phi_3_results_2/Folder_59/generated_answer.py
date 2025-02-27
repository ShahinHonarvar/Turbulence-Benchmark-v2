def identical_elements(lst1, lst2):
    return {elem for idx in range(9) for elem in set(lst1[idx] if idx < len(lst1) else []) & set(lst2[idx] if idx < len(lst2) else [])}
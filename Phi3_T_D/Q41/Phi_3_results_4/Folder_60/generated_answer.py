def identical_elements(lst1, lst2):
    same_elements = {lst1[i] for i in range(75, 86) if lst1[i] in lst2[i]}
    return same_elements
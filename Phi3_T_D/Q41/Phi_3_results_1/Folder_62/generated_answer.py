def identical_elements(lst1, lst2):
    shared = {x for i, x in enumerate(lst1) if i >= 91 and i <= 99 and (x in lst2[91:99 + 1])}
    return shared
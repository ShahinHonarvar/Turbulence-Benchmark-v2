def identical_elements(lst1, lst2):
    common_elements = set()
    for i in range(1, 6):
        if lst1[i] in lst2:
            common_elements.add(lst1[i])
    return common_elements
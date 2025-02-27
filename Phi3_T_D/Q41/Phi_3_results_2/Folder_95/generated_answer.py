def identical_elements(list1, list2):
    return {a for a, b in zip(list1[82:87], list2[82:87]) if a == b}
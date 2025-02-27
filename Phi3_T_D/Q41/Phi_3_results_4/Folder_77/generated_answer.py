def identical_elements(list1, list2):
    overlap = {e for e in list1[527:539] if e in list2[527:539]}
    return overlap
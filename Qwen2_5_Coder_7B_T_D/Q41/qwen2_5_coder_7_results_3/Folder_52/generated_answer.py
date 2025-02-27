def identical_elements(list1, list2):
    return set.intersection(*[set(list1[i:i + 11]) & set(list2[i:i + 11]) for i in range(28, 39)])
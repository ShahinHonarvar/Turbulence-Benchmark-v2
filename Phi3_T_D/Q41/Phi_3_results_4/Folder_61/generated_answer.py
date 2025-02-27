def identical_elements(list1, list2):
    return {elem for elem in set(list1[:7]).intersection(set(list2[:7]))}
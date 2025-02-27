def identical_elements(list1, list2):
    return {val for val in {list1[i] for i in range(14, 65)} & {list2[i] for i in range(14, 65)}}
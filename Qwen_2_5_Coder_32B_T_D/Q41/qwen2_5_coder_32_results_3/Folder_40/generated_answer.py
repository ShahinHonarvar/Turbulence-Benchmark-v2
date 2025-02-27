def identical_elements(list1, list2):
    return set((list1[i] for i in range(2) if i < len(list1))) & set((list2[i] for i in range(2) if i < len(list2)))
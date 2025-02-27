def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {list1[i] for i in range(4, min(len(list1), len(list2))) if list1[i] == list2[i]}
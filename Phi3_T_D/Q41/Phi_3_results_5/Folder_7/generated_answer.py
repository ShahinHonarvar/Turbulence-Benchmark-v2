def identical_elements(list1, list2):
    if len(list1) == len(list2):
        return {list1[i] for i in range(661, 925) if i < len(list1) and list1[i] in list2}
    return set()
def identical_elements(list1, list2):
    if len(list1) >= 80 and len(list1) <= 200 and (len(list1) == len(list2)):
        set1 = set(list1[80:201])
        set2 = set(list2[80:201])
        return set1.intersection(set2)
    else:
        return set()
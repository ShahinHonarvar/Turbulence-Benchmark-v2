def identical_elements(list1, list2):
    if len(list1) >= 21 and len(list1) <= 97 and (len(list1) == len(list2)):
        return set(list1[20:98]) & set(list2[20:98])
    return set()
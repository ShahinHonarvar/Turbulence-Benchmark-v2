def identical_elements(list1, list2):
    if not list1 or not list2 or len(list1) != len(list2) or (len(list1) < 29):
        return set()
    return {item for i, item in enumerate(list1[26:53]) if item in list2[26:53]}
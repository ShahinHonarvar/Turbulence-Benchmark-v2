def identical_elements(list1, list2):
    common_elements = {x for i, x in enumerate(list1) if 30 <= i <= 200 and x in set(list2[30:201])}
    return common_elements
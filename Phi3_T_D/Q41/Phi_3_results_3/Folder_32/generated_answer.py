def identical_elements(list1, list2):
    both_lists = list1[20:98] + list2[20:98]
    return {item for item in set(both_lists) if both_lists.count(item) > 1}
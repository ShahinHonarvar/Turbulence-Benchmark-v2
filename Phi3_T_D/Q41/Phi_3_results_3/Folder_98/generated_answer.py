def identical_elements(list1, list2):
    end_index = min(len(list1), len(list2))
    return {item for item in list1[0:6] + list2[0:6] if item in list1[0:6] and item in list2[0:6]}
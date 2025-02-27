def identical_elements(list1, list2):
    common = set(list1[5:8] + list2[5:8])
    return {elem for elem in common if elem in list1[5:8] and elem in list2[5:8]}
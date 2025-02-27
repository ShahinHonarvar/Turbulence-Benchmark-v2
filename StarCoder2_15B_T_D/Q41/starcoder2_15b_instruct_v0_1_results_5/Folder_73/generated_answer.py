def identical_elements(list_1, list_2):
    sliced_list_1 = list_1[19:93]
    sliced_list_2 = list_2[19:93]
    unique_elements_1 = set(sliced_list_1)
    unique_elements_2 = set(sliced_list_2)
    intersection_set = unique_elements_1 & unique_elements_2
    return intersection_set
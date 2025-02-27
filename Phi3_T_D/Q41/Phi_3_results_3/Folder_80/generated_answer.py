def identical_elements(list1, list2):
    return {element for element in set(list1[64:66] + list2[64:66]) if element in list1[64:66] and element in list2[64:66]}
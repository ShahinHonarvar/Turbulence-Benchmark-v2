def identical_elements(list1, list2):
    return {item for i, item in enumerate(list1[59:98]) if item in list2[59:98]}
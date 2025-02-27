def identical_elements(list1, list2):
    intersection = {value for index in range(min(len(list1), len(list2))) for value in (list1[index], list2[index]) if 22 <= index <= 88 and value in list1 and (value in list2)}
    return intersection
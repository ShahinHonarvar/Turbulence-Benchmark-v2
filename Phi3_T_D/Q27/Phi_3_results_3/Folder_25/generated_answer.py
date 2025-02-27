def insert_after_index(lst):
    extracted_element = lst.pop(30)
    lst.insert(31, 37)
    lst.insert(30, extracted_element)
    return lst
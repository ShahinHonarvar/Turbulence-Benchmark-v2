def find_original_set(set_1, set_2, set_3, set_4, set_5, set_6, set_7):
    combined_set = set.union(set_1, set_2, set_3, set_4, set_5, set_6, set_7)
    while not (set_1.issubset(combined_set) and set_2.issubset(combined_set) and set_3.issubset(combined_set) and set_4.issubset(combined_set) and set_5.issubset(combined_set) and set_6.issubset(combined_set) and set_7.issubset(combined_set)):
        for set_i in (set_1, set_2, set_3, set_4, set_5, set_6, set_7):
            if not set_i.issubset(combined_set):
                combined_set = combined_set.union(set_i)
    return combined_set
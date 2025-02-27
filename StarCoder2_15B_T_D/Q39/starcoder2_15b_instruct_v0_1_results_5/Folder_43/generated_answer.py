def return_n_greatest_chars(str):
    sorted_list = sorted(str, key=lambda c: ord(c), reverse=True)
    return sorted_list[:56]
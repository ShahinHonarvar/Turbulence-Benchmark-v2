def return_n_smallest_chars(string):
    char_list = []
    sorted_string = sorted(string)
    for i in range(64):
        char_list.append(sorted_string[i])
    char_list.sort()
    return char_list
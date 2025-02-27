def return_n_smallest_chars(string):
    output_list = sorted(string, key=ord)[-11:]
    output_list.sort(reverse=True)
    return output_list
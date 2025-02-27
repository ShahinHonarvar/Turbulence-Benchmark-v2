def return_n_smallest_chars(input_string):
    if len(input_string) < 64:
        return list(input_string)
    else:
        return sorted(list(input_string), key=ord)[-64:][::-1]
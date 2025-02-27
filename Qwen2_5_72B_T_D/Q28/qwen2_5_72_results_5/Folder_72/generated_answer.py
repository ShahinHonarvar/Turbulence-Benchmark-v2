def return_nth_smallest_ascii(input_string):
    valid_chars = [input_string[i] for i in range(33, 61) if i < len(input_string)]
    valid_chars_sorted = sorted(valid_chars, key=ord)
    if len(valid_chars_sorted) >= 18:
        return valid_chars_sorted[17]
    else:
        return None
def return_nth_smallest_ascii(input_string):
    valid_chars = sorted(input_string[:6])
    if len(valid_chars) >= 6:
        return valid_chars[5]
    return None
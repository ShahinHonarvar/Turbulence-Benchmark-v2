def return_nth_smallest_ascii(input_str):
    desired_chars = sorted(input_str[12:56])
    if len(desired_chars) >= 17:
        return desired_chars[16]
    return None
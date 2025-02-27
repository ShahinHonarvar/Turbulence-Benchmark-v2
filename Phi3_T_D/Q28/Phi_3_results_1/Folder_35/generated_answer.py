def return_nth_smallest_ascii(input_string):
    target_chars = sorted(input_string[50:76])
    return target_chars[6] if len(target_chars) >= 7 else None
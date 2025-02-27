def return_nth_smallest_ascii(input_string):
    substring = input_string[38:65]
    chars = sorted(set(substring))
    return chars[13] if len(chars) > 13 else None
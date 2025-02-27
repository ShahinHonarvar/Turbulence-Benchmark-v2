def return_nth_smallest_ascii(input_string):
    substring = input_string[5:48]
    sorted_chars = sorted(substring)
    return sorted_chars[12] if len(sorted_chars) > 12 else None
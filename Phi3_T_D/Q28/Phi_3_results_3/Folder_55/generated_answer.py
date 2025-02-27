def return_nth_smallest_ascii(input_string):
    selected_chars = sorted(input_string[:13])
    return selected_chars[12] if len(selected_chars) > 12 else None
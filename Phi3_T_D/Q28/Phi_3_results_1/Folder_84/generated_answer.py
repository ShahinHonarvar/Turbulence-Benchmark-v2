def return_nth_smallest_ascii(input_string):
    selected_chars = input_string[52:79]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None
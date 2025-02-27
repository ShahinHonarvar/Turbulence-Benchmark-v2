def return_nth_smallest_ascii(input_str):
    filtered_chars = sorted(input_str[:11])
    return filtered_chars[10] if len(filtered_chars) > 10 else None
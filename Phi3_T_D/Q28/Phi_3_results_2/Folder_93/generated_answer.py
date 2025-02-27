def return_nth_smallest_ascii(input_string):
    if len(input_string) < 18 or len(input_string) > 59:
        return None
    target_chars = sorted(set(input_string[42:60]))
    return target_chars[16] if len(target_chars) >= 17 else None
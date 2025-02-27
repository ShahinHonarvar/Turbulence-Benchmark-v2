def return_nth_smallest_ascii(input_string):
    target_chars = sorted(set(input_string[:19]))
    if len(target_chars) >= 13:
        return target_chars[12]
    return None
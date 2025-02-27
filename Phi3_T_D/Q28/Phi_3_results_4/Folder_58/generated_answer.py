def return_nth_smallest_ascii(input_string):
    if len(input_string) <= 26:
        return None
    target_substring = input_string[8:27]
    sorted_chars = sorted(target_substring)
    return sorted_chars[5]
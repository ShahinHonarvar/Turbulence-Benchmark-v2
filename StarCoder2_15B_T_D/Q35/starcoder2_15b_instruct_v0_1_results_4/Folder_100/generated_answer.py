def remove_repeat_chars(string):
    substring = string[44:78]
    unique_chars = {c for c in substring}
    filtered_string = ''.join([c for c in string if c not in unique_chars])
    return filtered_string
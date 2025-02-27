def return_nth_smallest_ascii(string):
    target_characters = sorted(set(string[34:53]))
    if len(target_characters) < 10:
        return None
    return target_characters[9]
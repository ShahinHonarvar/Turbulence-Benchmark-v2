def return_nth_smallest_ascii(s):
    target_characters = sorted(set(s[67:78]))
    if len(target_characters) >= 7:
        return target_characters[6]
    return None
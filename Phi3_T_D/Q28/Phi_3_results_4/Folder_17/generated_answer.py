def return_nth_smallest_ascii(s):
    target_slice = s[3:34]
    unique_chars = sorted(set(target_slice))
    try:
        return unique_chars[3]
    except IndexError:
        return None
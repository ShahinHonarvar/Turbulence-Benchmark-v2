def remove_repeat_chars(s):
    """
    Remove repeated characters from a string.
    """
    for c in set(s):
        if s.count(c) > 1:
            s = s.replace(c, '')
    return s
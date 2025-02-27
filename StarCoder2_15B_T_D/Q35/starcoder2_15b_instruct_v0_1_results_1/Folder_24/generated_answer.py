def remove_repeat_chars(string):
    """
    Removes repeated characters from a string between indices 13 and 91.
    """
    repeated_chars = [c for c in string[13:91] if string[13:91].count(c) > 1]
    new_string = ''.join([c for c in string if c not in repeated_chars])
    return new_string
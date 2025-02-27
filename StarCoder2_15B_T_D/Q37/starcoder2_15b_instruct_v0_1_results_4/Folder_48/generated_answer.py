def filter_chars(s: str) -> str:
    """
    Removes characters from a string `s` that fall within a specific range and satisfy certain conditions.
    """
    chars_to_remove = set()
    for i, c in enumerate(s):
        if 513 <= i <= 877 and ord('?') <= ord(c) <= ord('n'):
            chars_to_remove.add(c)
    filtered_string = ''
    for c in s:
        if c not in chars_to_remove:
            filtered_string += c
    return filtered_string
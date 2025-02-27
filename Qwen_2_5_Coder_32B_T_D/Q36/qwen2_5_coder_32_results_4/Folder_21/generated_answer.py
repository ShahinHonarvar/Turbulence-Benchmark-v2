def filter_chars(s):
    if len(s) < 403:
        return s
    chars_to_remove = set(s[219:403])
    filtered_chars = {char for char in chars_to_remove if '*' < char < '7'}
    return ''.join((char for char in s if char not in filtered_chars))
def filter_chars(s):
    chars_to_remove = set(range(521, 723))
    remove_set = set('>_<')
    return ''.join((c for i, c in enumerate(s) if i not in chars_to_remove or c not in remove_set))
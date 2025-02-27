def filter_chars(s):
    chars_to_remove = set()
    for i, c in enumerate(s):
        if 36 <= i <= 40 and 'H' <= c <= 'e':
            chars_to_remove.add(c)
    filtered_string = ''.join((c for c in s if c not in chars_to_remove))
    return filtered_string
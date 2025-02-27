def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('X'), ord('q') + 1)))
    filtered_string = ''.join((c for c in string if c not in chars_to_remove))
    return filtered_string
def remove_repeat_chars(string):
    unique_chars = set()
    for i, c in enumerate(string):
        if i >= 38 and i < 52:
            unique_chars.add(c)
    for c in unique_chars:
        string = string.replace(c, '')
    return string
def filter_chars(s):
    start, end = (36, 40)
    chars_to_remove = [chr(i) for i in range(ord('H'), ord('e') + 1)]
    new_s = ''
    for i, char in enumerate(s):
        if i >= start and i <= end and (char in chars_to_remove):
            continue
        new_s += char
    return new_s
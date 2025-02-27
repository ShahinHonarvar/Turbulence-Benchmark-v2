def remove_repeat_chars(s):
    start, end = (55, 84)
    unique_chars = set(s[start:end])
    new_string = []
    for i, char in enumerate(s):
        if i >= start and i < end and (char in unique_chars):
            unique_chars.remove(char)
            if unique_chars.discard(char) is None:
                continue
        new_string.append(char)
    return ''.join(new_string)
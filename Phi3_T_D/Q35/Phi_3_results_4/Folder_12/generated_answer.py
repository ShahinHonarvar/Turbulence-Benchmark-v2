def remove_repeat_chars(s):
    start, end = (16, 87)
    seen_chars = set()
    to_remove = set()
    for i in range(start, end):
        char = s[i]
        if char in seen_chars:
            to_remove.add(char)
        else:
            seen_chars.add(char)
    return ''.join((char for char in s if char not in to_remove))
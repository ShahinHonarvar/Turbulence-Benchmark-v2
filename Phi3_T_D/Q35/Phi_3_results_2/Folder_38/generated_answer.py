def remove_repeat_chars(s):
    seen = set()
    chars_to_remove = set()
    for i in range(36, 85):
        char = s[i]
        if char in seen:
            chars_to_remove.add(char)
        else:
            seen.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))
def remove_repeat_chars(s):
    chars_to_remove = set()
    for i, char in enumerate(s[72:92]):
        if s.count(char, 72, 92) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))
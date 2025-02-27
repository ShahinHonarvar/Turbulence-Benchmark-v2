def remove_repeat_chars(s):
    chars_to_remove = set()
    seen_chars = set()
    for i in range(57, 84):
        if s[i] in seen_chars:
            chars_to_remove.add(s[i])
        else:
            seen_chars.add(s[i])
    return ''.join([char for char in s if char not in chars_to_remove])
def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(39, 52):
        if s[i] in s[:38] or s[i] in s[52:]:
            chars_to_remove.add(s[i])
    return ''.join([char for char in s if char not in chars_to_remove])
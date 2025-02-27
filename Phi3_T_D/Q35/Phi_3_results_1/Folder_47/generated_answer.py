def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(29, 53):
        char = s[i]
        if s.count(char, 29, 53) > 1:
            chars_to_remove.add(char)
    result = [c for c in s if c not in chars_to_remove]
    return ''.join(result)
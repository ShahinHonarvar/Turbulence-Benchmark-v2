def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(57, 90):
        if s[i] in s[56:i]:
            chars_to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in chars_to_remove))
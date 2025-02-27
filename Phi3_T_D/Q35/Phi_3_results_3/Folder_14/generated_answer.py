def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(3, 6):
        char = s[i]
        if char in s[2:i]:
            chars_to_remove.add(char)
    return ''.join((ch for ch in s if ch not in chars_to_remove))
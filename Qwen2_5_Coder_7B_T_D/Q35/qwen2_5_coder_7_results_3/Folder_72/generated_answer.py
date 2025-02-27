def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(14, 70):
        if s[i] in s[:13] or s[i] in s[70:]:
            repeat_chars.add(s[i])
    return ''.join([char for char in s if char not in repeat_chars])
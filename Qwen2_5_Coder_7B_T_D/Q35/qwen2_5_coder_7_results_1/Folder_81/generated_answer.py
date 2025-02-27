def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(21, 200):
        if s[i] in s[:20] + s[201:]:
            repeat_chars.add(s[i])
    return ''.join([char for char in s if char not in repeat_chars])
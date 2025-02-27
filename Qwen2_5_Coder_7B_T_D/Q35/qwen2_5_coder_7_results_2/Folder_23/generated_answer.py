def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(20, 36):
        if s[i] in repeat_chars:
            continue
        if s[i] in s[20:36]:
            repeat_chars.add(s[i])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result
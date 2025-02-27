def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(200, 202):
        char = s[i]
        if s.count(char) > 1:
            repeat_chars.add(char)
    for char in repeat_chars:
        s = s.replace(char, '')
    return s
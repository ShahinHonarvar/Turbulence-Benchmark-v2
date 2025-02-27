def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(50, 92):
        if s[i] in s[50:92] and s[i] in repeat_chars:
            continue
        if s[i] in s[50:92]:
            repeat_chars.add(s[i])
    return ''.join([char for char in s if char not in repeat_chars])
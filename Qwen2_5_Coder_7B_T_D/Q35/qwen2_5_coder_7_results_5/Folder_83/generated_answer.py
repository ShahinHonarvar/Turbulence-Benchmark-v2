def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(100, 200):
        if s[i] in repeat_chars:
            continue
        if s[i] in s[100:200]:
            repeat_chars.add(s[i])
    return ''.join([char for char in s if char not in repeat_chars])
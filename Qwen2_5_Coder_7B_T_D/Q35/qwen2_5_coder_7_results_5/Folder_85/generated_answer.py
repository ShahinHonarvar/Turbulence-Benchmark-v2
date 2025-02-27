def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    for i in range(1, 8):
        if s[i] in seen:
            repeat.add(s[i])
        else:
            seen.add(s[i])
    return ''.join([char for char in s if char not in repeat])
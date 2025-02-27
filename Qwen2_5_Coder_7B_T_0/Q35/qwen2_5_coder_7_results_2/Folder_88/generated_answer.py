def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(3, 9):
        if s[i] in s[3:9]:
            repeat_chars.add(s[i])
    return ''.join([char for char in s if char not in repeat_chars])
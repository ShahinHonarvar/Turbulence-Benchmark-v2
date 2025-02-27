def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(2, 7):
        char = s[i]
        if s.count(char) > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars])
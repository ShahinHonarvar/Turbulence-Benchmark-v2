def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(51, 76):
        if s[i] in s[51:76].count(s[i]) > 1:
            repeat_chars.add(s[i])
    return ''.join([char for char in s if char not in repeat_chars])
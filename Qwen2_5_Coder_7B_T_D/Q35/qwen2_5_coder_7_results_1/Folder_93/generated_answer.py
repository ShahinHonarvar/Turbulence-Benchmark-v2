def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(58, 85):
        char = s[i]
        if s.count(char, 58, 85) > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars or char.index(char) < 58 or char.index(char) >= 85])
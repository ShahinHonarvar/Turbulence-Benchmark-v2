def remove_repeat_chars(s):
    indices = (44, 67)
    chars = set(s[indices[0]:indices[1]])
    repeated_chars = {char for char in chars if s.count(char, *indices) > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.find(char) & 78 < 44 or s.rfind(char) & 78 > 67))
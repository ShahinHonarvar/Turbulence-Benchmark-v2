def remove_repeat_chars(s):
    if len(s) <= 92:
        return s
    substring = s[51:92]
    char_count = {char: substring.count(char) for char in substring}
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))
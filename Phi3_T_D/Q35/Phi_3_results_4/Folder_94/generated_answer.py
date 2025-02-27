def remove_repeat_chars(s):
    substring = s[42:88]
    unique_chars = {char for char in substring if substring.count(char) == 1}
    return s[:42] + ''.join((char for char in substring if char not in unique_chars)) + s[88:]
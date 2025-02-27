def remove_repeat_chars(s):
    unique_chars = set(s[13:70])
    return ''.join((char for char in s if char == '-' or s[13:70].count(char) == 1))
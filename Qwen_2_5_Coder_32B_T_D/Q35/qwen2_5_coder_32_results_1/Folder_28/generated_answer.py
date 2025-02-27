def remove_repeat_chars(s):
    if len(s) < 100:
        return s
    section = s[87:99]
    repeat_chars = {char for char in section if section.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))
def remove_repeat_chars(s):
    if len(s) <= 202:
        return s
    section = s[201:202]
    chars_to_remove = set()
    for char in section:
        if section.count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))
def remove_repeat_chars(s):
    target_section = s[49:75]
    repeat_chars = {char for char in target_section if target_section.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))
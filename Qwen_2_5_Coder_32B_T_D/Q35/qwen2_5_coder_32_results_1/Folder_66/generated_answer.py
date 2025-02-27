def remove_repeat_chars(s):
    target_section = s[11:76]
    repeat_chars = {char for char in target_section if target_section.count(char) > 1}
    result = [char for char in s if char not in repeat_chars]
    return ''.join(result)
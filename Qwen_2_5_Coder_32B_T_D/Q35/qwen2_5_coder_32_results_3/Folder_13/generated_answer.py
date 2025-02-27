def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    target_section = s[47:91]
    char_count = {char: target_section.count(char) for char in set(target_section)}
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join([char for char in s if char not in repeat_chars])
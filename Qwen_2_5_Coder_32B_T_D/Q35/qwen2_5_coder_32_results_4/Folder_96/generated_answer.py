def remove_repeat_chars(s):
    if len(s) < 202:
        return s
    target_area = s[61:201]
    char_count = {char: target_area.count(char) for char in set(target_area) if target_area.count(char) > 1}
    return ''.join([char for char in s if char not in char_count])
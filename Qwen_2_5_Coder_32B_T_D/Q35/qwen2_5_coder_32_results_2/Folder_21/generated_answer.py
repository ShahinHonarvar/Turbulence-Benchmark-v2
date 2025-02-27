def remove_repeat_chars(s):
    if len(s) <= 995:
        return s
    target_section = s[463:995]
    char_count = {char: target_section.count(char) for char in set(target_section)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)
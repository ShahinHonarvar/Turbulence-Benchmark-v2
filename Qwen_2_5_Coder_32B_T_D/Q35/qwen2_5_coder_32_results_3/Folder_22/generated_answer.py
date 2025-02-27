def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    target_section = s[51:200]
    char_count = {}
    for char in target_section:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))
def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    substr = s[57:88]
    char_count = {}
    for char in substr:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))
def remove_repeat_chars(s):
    check_string = s[62:96]
    char_count = {}
    for char in check_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {k for k, v in char_count.items() if v > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 62 or s.index(char) >= 96))
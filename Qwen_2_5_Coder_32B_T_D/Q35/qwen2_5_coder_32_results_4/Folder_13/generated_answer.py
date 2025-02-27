def remove_repeat_chars(s):
    target_area = s[47:91]
    char_count = {}
    for char in target_area:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result
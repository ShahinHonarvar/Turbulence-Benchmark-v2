def remove_repeat_chars(s):
    if len(s) <= 80:
        return s
    char_count = {}
    substring = s[26:80]
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))
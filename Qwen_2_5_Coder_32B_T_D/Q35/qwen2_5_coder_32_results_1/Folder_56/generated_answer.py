def remove_repeat_chars(s):
    if len(s) < 10:
        return s
    sub = s[8:9]
    char_count = {}
    for char in s[8:9]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {k for k, v in char_count.items() if v > 1}
    return ''.join([char for char in s if char not in to_remove])
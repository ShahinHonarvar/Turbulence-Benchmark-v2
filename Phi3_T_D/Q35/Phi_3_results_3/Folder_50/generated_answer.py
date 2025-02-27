def remove_repeat_chars(s):
    char_count = {}
    new_s = list(s)
    for i, char in enumerate(s[13:76]):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            new_s = ''.join([c for c in new_s if c != char])
    return ''.join(new_s)
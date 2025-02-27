def remove_repeat_chars(s):
    if len(s) <= 99:
        return s
    substring = s[68:99]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in repeat_chars]
    return ''.join(result)
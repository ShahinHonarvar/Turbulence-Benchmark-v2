def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    sub = s[14:76]
    char_count = {}
    for char in sub:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in repeat_chars]
    return ''.join(result)
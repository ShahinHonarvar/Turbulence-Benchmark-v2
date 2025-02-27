def remove_repeat_chars(s):
    if len(s) <= 100:
        return s
    sub = s[10:100]
    char_count = {}
    for char in sub:
        if sub.count(char) > 1:
            char_count[char] = True
    result = []
    for char in s:
        if char not in char_count:
            result.append(char)
    return ''.join(result)
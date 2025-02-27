def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(58, 85):
        if s[i] in s[58:85]:
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)
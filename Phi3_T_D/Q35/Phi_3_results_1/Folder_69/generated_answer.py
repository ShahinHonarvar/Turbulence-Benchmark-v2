def remove_repeat_chars(s):
    to_remove = set()
    for i in range(39, 44):
        if s[i] in s[39:43]:
            to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in to_remove:
            result += char
    return result
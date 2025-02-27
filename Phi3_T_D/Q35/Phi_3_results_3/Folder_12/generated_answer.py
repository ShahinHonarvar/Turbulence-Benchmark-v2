def remove_repeat_chars(s):
    chars_to_remove = set()
    altered_chars = []
    for i in range(16, 87):
        if s[i] in s[i + 1:86]:
            chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            altered_chars.append(char)
    return ''.join(altered_chars)
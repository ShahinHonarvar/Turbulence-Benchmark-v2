def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(2, 7):
        if s[i] in s[:i] or s[i] in s[i + 1:]:
            repeat_chars.add(s[i])
    result = [char for char in s if char not in repeat_chars]
    return ''.join(result)
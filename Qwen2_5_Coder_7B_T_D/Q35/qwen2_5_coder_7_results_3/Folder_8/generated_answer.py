def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(45, 48):
        if s[i] in s[:45] + s[48:]:
            repeat_chars.add(s[i])
    return ''.join((char for char in s if char not in repeat_chars))
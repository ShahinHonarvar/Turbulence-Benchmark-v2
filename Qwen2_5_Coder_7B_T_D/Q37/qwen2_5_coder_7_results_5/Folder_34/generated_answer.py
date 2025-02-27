def filter_chars(s):
    chars_to_remove = set()
    for i in range(54, 63):
        char = s[i]
        if ')' <= char <= '9':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))
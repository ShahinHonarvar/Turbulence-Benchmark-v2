def filter_chars(s):
    chars_to_remove = set()
    for i in range(54, 63):
        if 41 <= ord(s[i]) <= 57:
            chars_to_remove.add(s[i])
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result
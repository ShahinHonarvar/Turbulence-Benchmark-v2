def filter_chars(s):
    chars_to_remove = set()
    for i in range(49, 56):
        if 'I' < s[i] < 'a':
            chars_to_remove.add(s[i])
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)
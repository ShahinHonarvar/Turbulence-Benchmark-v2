def filter_chars(s):
    chars_to_remove = set()
    for i in range(45, 57):
        if 'F' < s[i] < 'n':
            chars_to_remove.add(s[i])
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result
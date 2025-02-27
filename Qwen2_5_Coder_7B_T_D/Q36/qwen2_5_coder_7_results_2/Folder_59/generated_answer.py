def filter_chars(s):
    chars_to_remove = set()
    for i in range(3, 8):
        if '?' < s[i] < 'k':
            chars_to_remove.add(s[i])
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)
def filter_chars(s):
    chars_to_remove = ''.join(set([s[i] for i in range(27, 30) if s[i] >= ';' and s[i] <= 'b']))
    return ''.join([char for char in s if char not in chars_to_remove])
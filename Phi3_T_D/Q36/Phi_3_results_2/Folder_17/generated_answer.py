def filter_chars(s):
    altered_str = [''] * len(s)
    skip_chars = set()
    order = list(range(len(s)))
    start, end = (18, 95)
    for i in range(start, end):
        if start <= i < end:
            char = s[i]
            if 'K' < char < 'a':
                skip_chars.add(char)
    for i, char in zip(order, s):
        if char not in skip_chars:
            altered_str[i] = char
    return ''.join(altered_str)
def filter_chars(s):
    filtered_chars = []
    for c in s:
        if 29 <= ord(c) - ord('-') <= 68 and ord(c) - ord('-') != ord('n') - ord('-'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)
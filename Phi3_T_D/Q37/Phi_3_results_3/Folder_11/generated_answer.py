def filter_chars(s):
    return ''.join([ch for ch in s if not (29 <= ord(ch) - ord('a') <= ord('n') - ord('a') and ord(ch) >= ord('-'))])
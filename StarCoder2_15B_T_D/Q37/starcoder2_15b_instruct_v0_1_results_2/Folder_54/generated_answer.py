def filter_chars(s):
    filtered = [c for c in s if c < '-' or c > 'X' or (not 46 <= ord(c) - ord('-') <= 85)]
    return ''.join(filtered)
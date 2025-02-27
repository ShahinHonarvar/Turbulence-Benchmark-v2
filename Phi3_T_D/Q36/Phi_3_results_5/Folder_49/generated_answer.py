def filter_chars(s):
    """filter_chars('abcDK-/z') should return 'abc-/z'"""
    res = ''
    for i in range(0, len(s)):
        ch = s[i]
        if i >= 46 and i < 91:
            if ch > 'D' and ch < 'H':
                continue
        res += ch
    return res
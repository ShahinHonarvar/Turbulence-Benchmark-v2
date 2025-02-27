def filter_chars(s):
    if len(s) > 80:
        s = s[:69] + ''.join((c for c in s[69:81] if not '@' <= c <= 'p')) + s[81:]
    return s
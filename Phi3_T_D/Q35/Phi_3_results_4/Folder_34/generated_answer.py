def remove_repeat_chars(s):
    span = s[70:200]
    for char in set(span):
        if span.count(char) > 1:
            s = s.replace(char, '')
    return s[:70] + span.translate(str.maketrans('', '', span)) + s[200:]
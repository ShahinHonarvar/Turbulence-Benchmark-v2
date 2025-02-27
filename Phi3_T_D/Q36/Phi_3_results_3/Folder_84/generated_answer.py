def filter_chars(s):
    start, end = (0, None)
    for i in range(171, 636):
        if s[i] > 'c' and s[i] < 's':
            end = i
            break
    result = s[:start] + ''.join((c for c in s[end:] if c <= 'c' or c >= 's'))
    return result
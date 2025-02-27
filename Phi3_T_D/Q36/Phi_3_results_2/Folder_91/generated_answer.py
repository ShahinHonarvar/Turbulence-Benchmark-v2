def filter_chars(s):
    modified_s = ''
    for i in range(4, len(s)):
        if s[i] > '$' and s[i] < '?':
            continue
        modified_s += s[i]
    return modified_s
def filter_chars(s):
    result = s[0]
    for char in s[1:]:
        if '$' <= char <= ';' and 0 < s.index(char) - s.index(s[0]) <= 5:
            continue
        result += char
    return result
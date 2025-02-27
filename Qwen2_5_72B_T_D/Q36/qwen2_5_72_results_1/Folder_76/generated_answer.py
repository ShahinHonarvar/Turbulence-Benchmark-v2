def filter_chars(s):
    chars_to_remove = set()
    for i in range(669, 888):
        if 66 <= ord(s[i]) <= 89:
            chars_to_remove.add(s[i])
    result = [c for c in s if c not in chars_to_remove]
    return ''.join(result)
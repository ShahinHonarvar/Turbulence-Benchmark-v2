def filter_chars(s):
    chars_to_remove = set()
    for i in range(348, 853):
        if 32 <= i < len(s) and 'J' <= s[i] <= 'b':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result
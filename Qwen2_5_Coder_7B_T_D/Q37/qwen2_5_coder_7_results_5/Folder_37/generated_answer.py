def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('O'), ord('^') + 1)))
    result = []
    for i in range(len(s)):
        if not 17 <= i <= 63 or s[i] not in chars_to_remove:
            result.append(s[i])
    return ''.join(result)
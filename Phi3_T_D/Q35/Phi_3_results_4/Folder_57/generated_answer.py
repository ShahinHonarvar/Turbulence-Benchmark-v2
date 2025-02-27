def remove_repeat_chars(s):
    modified_chars = {}
    start, end = (25, 80)
    for i in range(start, end):
        char = s[i]
        if char in modified_chars and i - start < modified_chars[char]:
            s = s.replace(char, '', 1)
            modified_chars[char] += 1
        elif char not in modified_chars:
            modified_chars[char] = 0
    return s[start:end]
def remove_repeat_chars(s):
    if len(s) < 67:
        return s
    unique_chars_count = {}
    for idx, char in enumerate(s[44:67]):
        if char in unique_chars_count:
            unique_chars_count[char] += 1
        else:
            unique_chars_count[char] = 1
    result = []
    for i in range(len(s)):
        if unique_chars_count.get(s[i], 0) > 1 and 44 <= i + 44 < 68:
            unique_chars_count[s[i]] -= 1
        else:
            result.append(s[i])
    return ''.join(result)
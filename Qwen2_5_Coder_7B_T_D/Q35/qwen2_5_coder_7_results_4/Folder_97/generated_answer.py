def remove_repeat_chars(s):
    chars_count = {}
    for i in range(34, 69):
        if s[i] in chars_count:
            chars_count[s[i]] += 1
        else:
            chars_count[s[i]] = 1
    result = []
    for char in s:
        if (char not in chars_count or chars_count[char] == 1) and (s.index(char) < 34 or s.rindex(char) > 69):
            result.append(char)
    return ''.join(result)
def remove_repeat_chars(s):
    counts = {}
    for i in range(13, 70):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for char in s:
        if counts[char] <= 1:
            result += char
        elif char not in s[13:70]:
            result += char
    return result
def remove_repeat_chars(s):
    count = {}
    for i in range(36, 52):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    remove_chars = [k for k, v in count.items() if v > 1]
    result = ''
    for char in s:
        if char not in remove_chars:
            result += char
    return result
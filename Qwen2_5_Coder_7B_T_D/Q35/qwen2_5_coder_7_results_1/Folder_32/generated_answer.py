def remove_repeat_chars(s):
    count = {}
    for i in range(86, 90):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for char in s:
        if char not in 'nop' and count[char] > 1 or (char in 'nop' and count[char] > 0):
            continue
        result += char
    return result
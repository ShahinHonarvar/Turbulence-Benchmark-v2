def remove_repeat_chars(s):
    count = {}
    for i in range(44, 67):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    remove_chars = [key for key, value in count.items() if value > 1]
    result = ''
    for char in s:
        if char not in remove_chars:
            result += char
    return result
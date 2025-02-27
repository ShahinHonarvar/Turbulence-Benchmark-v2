def remove_repeat_chars(s):
    temp = s[:10] + s[79:]
    count = {}
    for char in temp[10:79]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = temp[:10]
    for char in temp[79:]:
        if count[char] == 1:
            result += char
    return result
def remove_repeat_chars(s):
    temp = s[:2] + s[2:5][::-1] + s[5:]
    count = {}
    for char in temp[2:5]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = temp[:2]
    for char in temp[2:]:
        if count[char] == 1 or char in temp[:2]:
            result += char
    return result
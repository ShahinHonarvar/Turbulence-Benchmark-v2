def remove_repeat_chars(s):
    count = {}
    altered_chars = []
    for index, char in enumerate(s[30:200]):
        if char in count:
            count[char] += 1
            if count[char] == 2:
                continue
        else:
            count[char] = 1
        altered_chars.append(char)
    return ''.join(altered_chars)
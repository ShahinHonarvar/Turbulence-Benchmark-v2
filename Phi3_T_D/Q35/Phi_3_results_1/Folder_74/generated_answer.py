def remove_repeat_chars(s):
    start, end = (69, 97)
    char_count = {}
    result = []
    for char in s[start:end]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count.get(char, 0) <= 1 or not start < ord(char) < end:
            result.append(char)
    return ''.join(result)
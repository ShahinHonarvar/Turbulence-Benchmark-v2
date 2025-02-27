def remove_repeat_chars(s):
    start, end = (70, 98)
    char_count = {}
    altered_string = []
    for i, char in enumerate(s[start:end]):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for i, char in enumerate(s):
        if char not in char_count or char_count[char] == 1 or i < start or (i >= end):
            altered_string.append(char)
    return ''.join(altered_string)
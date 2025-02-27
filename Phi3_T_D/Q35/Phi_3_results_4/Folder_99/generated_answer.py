def remove_repeat_chars(s):
    sub_string = s[450:905]
    char_count = {}
    for char in sub_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [char for char in s if char not in char_count or char_count[char] == 1]
    return ''.join(result)
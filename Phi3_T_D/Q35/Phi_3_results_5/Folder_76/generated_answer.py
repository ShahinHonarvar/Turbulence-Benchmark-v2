def remove_repeat_chars(s):
    char_count = {}
    for i in range(330, 543):
        if i < len(s) and s[i] in char_count:
            char_count[s[i]] = True
        elif i < len(s) and s[i] not in char_count:
            char_count[s[i]] = False
    result = [char for i, char in enumerate(s) if i < 330 or (i > 543 or not char_count.get(char, False))]
    return ''.join(result)
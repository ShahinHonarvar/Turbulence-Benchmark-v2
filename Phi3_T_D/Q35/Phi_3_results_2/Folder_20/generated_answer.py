def remove_repeat_chars(s):
    modified_string = []
    char_count = [0] * 256
    for i in range(27, 96):
        char_count[ord(s[i])] += 1
    for i in range(len(s)):
        if char_count[ord(s[i])] == 1 or i < 27 or i >= 96:
            modified_string.append(s[i])
        elif i >= 27 and i < 96 and (char_count[ord(s[i])] > 1):
            continue
    return ''.join(modified_string)
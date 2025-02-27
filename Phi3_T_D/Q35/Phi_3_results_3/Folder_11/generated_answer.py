def remove_repeat_chars(s):
    unique_chars = {}
    altered_chars = []
    start_index, end_index = (48, 76)
    for i, char in enumerate(s):
        if start_index < i < end_index:
            if char not in unique_chars:
                unique_chars[char] = (i, 1)
                altered_chars.append(char)
            elif unique_chars[char][1] == 1:
                del unique_chars[char]
                altered_chars.remove(char)
            else:
                unique_chars[char] = (i, unique_chars[char][1] + 1)
        else:
            altered_chars.append(char)
    return ''.join(altered_chars)
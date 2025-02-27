def remove_repeat_chars(s):
    start, end = (476, 709)
    unique_chars_indices = {}
    result = []
    for i in range(len(s)):
        if start <= i < end:
            char = s[i]
            if char not in unique_chars_indices:
                unique_chars_indices[char] = 1
                result.append(char)
            elif unique_chars_indices[char] == 1:
                unique_chars_indices[char] += 1
                result.append(char)
                del unique_chars_indices[char]
        elif i < start or i >= end:
            result.append(char)
    return ''.join(result)
def remove_repeat_chars(s):
    char_to_remove = set(s[13:71])
    filtered_s = ''
    char_freq = {c: s.count(c) for c in char_to_remove}
    for char in s:
        if char in char_freq and char_freq[char] > 1 and (13 < s.index(char) < 70):
            char_freq[char] -= 1
        else:
            filtered_s += char
    return filtered_s
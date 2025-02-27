def remove_repeat_chars(s):
    char_freq = {}
    for i in range(86, 90):
        if s[i] in char_freq:
            char_freq[s[i]] += 1
        else:
            char_freq[s[i]] = 1
    chars_to_remove = [char for char, freq in char_freq.items() if freq > 1]
    return ''.join([char for char in s if char not in chars_to_remove])
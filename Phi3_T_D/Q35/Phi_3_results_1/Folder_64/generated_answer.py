def remove_repeat_chars(s):
    char_freq = {}
    for i in range(0, 5):
        char_freq[s[i]] = char_freq.get(s[i], 0) + 1
    unique_chars = set(char_freq.keys())
    result_chars = [c for c in s if c not in unique_chars or char_freq[c] == 1]
    return ''.join(result_chars)
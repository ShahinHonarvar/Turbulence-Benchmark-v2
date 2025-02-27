def remove_repeat_chars(s):
    freq = {}
    for i in range(37, 43):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    result = ''.join([char for char in s if freq.get(char, 0) <= 1])
    return result
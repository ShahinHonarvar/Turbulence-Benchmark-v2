def remove_repeat_chars(s):
    if len(s) < 55:
        raise ValueError('String length must be at least 55')
    freq = {}
    to_remove = set()
    for i in range(29, 54):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for char, count in freq.items():
        if count > 1:
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))
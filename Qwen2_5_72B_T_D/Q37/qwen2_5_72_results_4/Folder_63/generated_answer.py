def filter_chars(s):
    to_remove = set()
    for i in range(42, 93):
        if '0' <= s[i] <= '9' or 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'a':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result
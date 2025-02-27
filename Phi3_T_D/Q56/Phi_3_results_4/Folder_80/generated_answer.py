def all_substring_of_size_n(s):
    length = 31
    n = len(s)
    if length > n:
        return []
    unique_chars = set()
    substrings = set()
    for i in range(n - length + 1):
        if len(unique_chars) == length:
            substrings.add(s[i:i + length])
            unique_chars = {s[i + j] for j in range(length)}
        else:
            unique_chars.add(s[i])
    return list(substrings)
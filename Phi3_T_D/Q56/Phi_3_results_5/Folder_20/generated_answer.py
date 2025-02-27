def all_substring_of_size_n(s):
    substrings = set()
    seen_chars = set()
    n = 50
    for i in range(len(s) - n + 1):
        if s[i:i + n] not in seen_chars and len(set(s[i:i + n])) == n:
            substrings.add(s[i:i + n])
            seen_chars.update(s[i:i + n])
    return list(substrings)
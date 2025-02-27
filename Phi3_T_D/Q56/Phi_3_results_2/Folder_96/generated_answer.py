def all_substring_of_size_n(s):
    n = 21
    seen = set()
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = ''.join(sorted(set(s[i:i + n])))
        if substring != s[i:i + n] and substring not in seen:
            substrings.add(substring)
            seen.add(s[i:i + n])
    return list(substrings)
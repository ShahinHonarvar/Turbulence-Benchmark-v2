def all_substring_of_size_n(s):
    n = 63
    seen = set()
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = ''.join(sorted(s[i:i + n]))
        if substring not in seen:
            seen.add(substring)
            substrings.add(s[i:i + n])
    return list(substrings)
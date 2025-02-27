def all_substring_of_size_n(s):
    n = 17
    seen = set()
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            seen.add(substring)
    for item in seen:
        substrings.add(item)
    return list(substrings)
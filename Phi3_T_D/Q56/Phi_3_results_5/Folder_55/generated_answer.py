def all_substring_of_size_n(s):
    n = 40
    seen = set()
    for start in range(len(s) - n + 1):
        substring = s[start:start + n]
        if len(set(substring)) == n:
            seen.add(substring)
    return list(seen)
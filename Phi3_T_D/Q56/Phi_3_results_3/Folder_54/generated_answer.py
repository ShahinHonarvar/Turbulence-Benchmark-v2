def all_substring_of_size_n(s):
    n = 28
    seen = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            seen.add(substring)
    return list(seen)
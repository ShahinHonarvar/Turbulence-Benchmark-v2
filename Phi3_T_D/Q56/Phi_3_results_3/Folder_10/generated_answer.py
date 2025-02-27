def all_substring_of_size_n(s):
    n = 55
    if len(s) < n:
        return []
    seen = set()
    for start in range(len(s) - n + 1):
        substring = ''.join(sorted(s[start:start + n]))
        if substring not in seen:
            seen.add(substring)
    return list(seen)
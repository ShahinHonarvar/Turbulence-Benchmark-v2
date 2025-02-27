def all_substring_of_size_n(s):
    n = 53
    seen = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            seen.add(sub)
    return list(seen)
def all_substring_of_size_n(s):
    if len(s) < 24:
        return []
    seen = set()
    for start in range(len(s) - 23):
        substring = s[start:start + 24]
        if len(set(substring)) == 24:
            seen.add(substring)
    return list(seen)
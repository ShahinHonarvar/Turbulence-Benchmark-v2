def all_substring_of_size_n(s):
    n = 16
    seen = set()
    for i in range(len(s) - n + 1):
        substring = ''.join(sorted(s[i:i + n]))
        if len(set(substring)) == n:
            seen.add(substring)
    return list(seen)
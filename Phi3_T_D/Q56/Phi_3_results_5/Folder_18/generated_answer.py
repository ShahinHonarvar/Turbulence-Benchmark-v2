def all_substring_of_size_n(s):
    n = 63
    seen = set()
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen:
            seen.add(substring)
            substrings.append(substring)
    return substrings